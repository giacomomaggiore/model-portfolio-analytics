"""Build a transparent historical approximation of the NTSG index."""

import csv
from datetime import date
from pathlib import Path
from urllib.request import Request, urlopen


DATA_DIR = Path(__file__).resolve().parent.parent / "data"
FRED_URL = "https://fred.stlouisfed.org/graph/fredgraph.csv?id=DGS3MO"
EQUITY_TER = 0.0024
BOND_TER = 0.0005
NTSG_TER = 0.0025


def read_prices(filename: str) -> dict[date, float]:
    """Read a project adjusted-price CSV into a date-keyed series."""
    with (DATA_DIR / filename).open(newline="") as file:
        return {
            date.fromisoformat(row["date"]): float(row["adjusted_price"])
            for row in csv.DictReader(file)
        }


def download_cash_rates() -> dict[date, float]:
    """Download the annualized three-month Treasury rate from FRED."""
    request = Request(FRED_URL, headers={"User-Agent": "model-portfolio-backtest/1.0"})
    with urlopen(request, timeout=30) as response:
        rows = csv.DictReader(response.read().decode().splitlines())
        return {
            date.fromisoformat(row["observation_date"]): float(row["DGS3MO"])
            for row in rows
            if row["DGS3MO"] not in ("", ".")
        }


def quarter(value: date) -> tuple[int, int]:
    """Return the calendar quarter used for the index proxy rebalance."""
    return value.year, (value.month - 1) // 3 + 1


def write_prices(filename: str, values: dict[date, float]) -> None:
    """Write a project adjusted-price CSV."""
    with (DATA_DIR / filename).open("w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(("date", "adjusted_price"))
        writer.writerows((value.isoformat(), f"{price:.10f}") for value, price in values.items())


def build_cash_index(dates: list[date], annualized_rates: dict[date, float]) -> dict[date, float]:
    """Compound the latest available DGS3MO annualized rate over calendar days."""
    cash_index = {dates[0]: 100.0}
    latest_rate = annualized_rates.get(dates[0])
    if latest_rate is None:
        raise ValueError("No DGS3MO observation is available on the proxy start date.")

    for previous_date, current_date in zip(dates, dates[1:]):
        elapsed_days = (current_date - previous_date).days
        cash_index[current_date] = cash_index[previous_date] * (1 + latest_rate / 100 / 365) ** elapsed_days
        latest_rate = annualized_rates.get(current_date, latest_rate)
    return cash_index


def gross_index(prices: dict[date, float], dates: list[date], ter: float) -> dict[date, float]:
    """Approximately remove an ETF's fee drag from adjusted-price returns."""
    result = {dates[0]: 100.0}
    for previous_date, current_date in zip(dates, dates[1:]):
        elapsed_days = (current_date - previous_date).days
        fee_factor = (1 - ter / 365) ** elapsed_days
        net_return_factor = prices[current_date] / prices[previous_date]
        result[current_date] = result[previous_date] * net_return_factor / fee_factor
    return result


def excess_return_index(
    total_return_index: dict[date, float],
    cash_index: dict[date, float],
    dates: list[date],
) -> dict[date, float]:
    """Convert a funded total-return index into a futures-style excess-return index."""
    result = {dates[0]: 100.0}
    for previous_date, current_date in zip(dates, dates[1:]):
        total_return_factor = total_return_index[current_date] / total_return_index[previous_date]
        cash_return_factor = cash_index[current_date] / cash_index[previous_date]
        result[current_date] = result[previous_date] * total_return_factor / cash_return_factor
    return result


def build_capital_efficient_proxy(
    dates: list[date],
    funded_indices: dict[str, tuple[float, dict[date, float]]],
    futures_indices: dict[str, tuple[float, dict[date, float]]],
    cash_weight: float,
    cash_index: dict[date, float],
    annual_fee: float,
) -> dict[date, float]:
    """Combine funded assets, cash collateral, and futures P&L with quarterly resets."""
    values = {dates[0]: 100.0}
    funded_units = {
        name: weight * values[dates[0]] / index[dates[0]]
        for name, (weight, index) in funded_indices.items()
    }
    futures_units = {
        name: weight * values[dates[0]] / index[dates[0]]
        for name, (weight, index) in futures_indices.items()
    }
    cash_units = cash_weight * values[dates[0]] / cash_index[dates[0]]

    for previous_date, current_date in zip(dates, dates[1:]):
        previous_value = values[previous_date]
        if quarter(current_date) != quarter(previous_date):
            funded_units = {
                name: weight * previous_value / index[previous_date]
                for name, (weight, index) in funded_indices.items()
            }
            futures_units = {
                name: weight * previous_value / index[previous_date]
                for name, (weight, index) in futures_indices.items()
            }
            cash_units = cash_weight * previous_value / cash_index[previous_date]

        funded_value = sum(
            funded_units[name] * index[current_date]
            for name, (_, index) in funded_indices.items()
        )
        cash_value = cash_units * cash_index[current_date]
        futures_profit = sum(
            futures_units[name] * (index[current_date] - index[previous_date])
            for name, (_, index) in futures_indices.items()
        )
        pre_fee_value = funded_value + cash_value + futures_profit
        elapsed_days = (current_date - previous_date).days
        fee_factor = (1 - annual_fee / 365) ** elapsed_days
        fee = pre_fee_value * (1 - fee_factor)
        cash_value += futures_profit - fee
        cash_units = cash_value / cash_index[current_date]
        values[current_date] = funded_value + cash_value

    return values


def build_proxy(annualized_rates: dict[date, float]) -> dict[date, float]:
    """Combine developed equities, global bonds, and USD cash with quarterly resets."""
    equity_prices = read_prices("URTH.CSV")
    bond_prices = read_prices("BNDW.CSV")
    dates = sorted(equity_prices.keys() & bond_prices.keys())
    if not dates:
        raise ValueError("URTH and BNDW do not have overlapping observations.")

    cash_index = build_cash_index(dates, annualized_rates)
    gross_equity = gross_index(equity_prices, dates, EQUITY_TER)
    gross_bonds = gross_index(bond_prices, dates, BOND_TER)
    bond_excess_return = excess_return_index(gross_bonds, cash_index, dates)
    proxy = build_capital_efficient_proxy(
        dates,
        {"equity": (0.9, gross_equity)},
        {"bonds": (0.6, bond_excess_return)},
        0.1,
        cash_index,
        NTSG_TER,
    )

    write_prices("USD_CASH.CSV", cash_index)
    return proxy


def build_extended_proxy(annualized_rates: dict[date, float]) -> dict[date, float]:
    """Build the longer, lower-fidelity NTSG proxy from 2007 ETF inputs."""
    components = {
        "SPY": (0.630, 0.000945),
        "EFA": (0.243, 0.0032),
        "EWC": (0.027, 0.0050),
        "IEF": (0.300, 0.0015),
        "BWX": (0.300, 0.0035),
    }
    price_series = {ticker: read_prices(f"{ticker}.CSV") for ticker in components}
    dates = sorted(set.intersection(*(set(prices) for prices in price_series.values())))
    if not dates:
        raise ValueError("The extended proxy components do not have overlapping observations.")

    cash_index = build_cash_index(dates, annualized_rates)
    gross_indices = {
        ticker: gross_index(price_series[ticker], dates, ter)
        for ticker, (_, ter) in components.items()
    }
    bond_excess_indices = {
        ticker: excess_return_index(gross_indices[ticker], cash_index, dates)
        for ticker in ("IEF", "BWX")
    }
    funded_indices = {
        ticker: (weight, gross_indices[ticker])
        for ticker, (weight, _) in components.items()
        if ticker in ("SPY", "EFA", "EWC")
    }
    futures_indices = {
        ticker: (components[ticker][0], bond_excess_indices[ticker])
        for ticker in bond_excess_indices
    }
    return build_capital_efficient_proxy(
        dates,
        funded_indices,
        futures_indices,
        0.1,
        cash_index,
        NTSG_TER,
    )


def main() -> None:
    DATA_DIR.mkdir(exist_ok=True)
    annualized_rates = download_cash_rates()
    proxy = build_proxy(annualized_rates)
    extended_proxy = build_extended_proxy(annualized_rates)
    write_prices("NTSG_proxy.csv", proxy)
    write_prices("NTSG_proxy_extended.csv", extended_proxy)
    print(f"Wrote NTSG_proxy.csv: {len(proxy)} rows")
    print(f"Wrote NTSG_proxy_extended.csv: {len(extended_proxy)} rows")


if __name__ == "__main__":
    main()