"""Validate proxy outputs and write monthly correlation panels."""

import csv
import math
from datetime import date
from pathlib import Path
from statistics import fmean


PROJECT_ROOT = Path(__file__).resolve().parent.parent
DATA_DIR = PROJECT_ROOT / "data"
OUTPUT_DIR = PROJECT_ROOT / "outputs"

PANELS = {
    "actual_etfs": {
        "NTSG": "NTSG.CSV",
        "COM": "COM.CSV",
        "DBMF": "DBMF.CSV",
        "GDE": "GDE.CSV",
        "TAIL": "TAIL.CSV",
        "MSCI_WORLD_USD": "MSCI_WORLD_USD.CSV",
    },
    "synthetic_sensitivity": {
        "NTSG_SYNTHETIC": "NTSG_proxy_extended.csv",
        "COM_ABCTRI_PROXY": "COM_proxy.csv",
        "WTMF_AS_DBMF_PEER": "DBMF_proxy.csv",
        "GDE_SYNTHETIC": "GDE_proxy.csv",
        "PPUT_BENCHMARK": "PPUT.CSV",
        "MSCI_WORLD_USD": "MSCI_WORLD_USD.CSV",
    },
    "underlying_exposures": {
        "GLOBAL_EQUITY": "MSCI_WORLD_USD.CSV",
        "GLOBAL_BONDS": "BNDW.CSV",
        "COMMODITIES": "PDBC.CSV",
        "MANAGED_FUTURES": "WTMF.CSV",
        "US_LARGE_CAP": "SPY.CSV",
        "GOLD": "GLD.CSV",
        "TAIL_STRATEGY": "TAIL.CSV",
    },
}

PROXY_VALIDATIONS = {
    "NTSG": ("NTSG_proxy.csv", "NTSG.CSV"),
    "GDE": ("GDE_proxy.csv", "GDE.CSV"),
    "COM": ("COM_proxy.csv", "COM.CSV"),
    "DBMF": ("DBMF_proxy.csv", "DBMF.CSV"),
}


def read_prices(filename: str) -> dict[date, float]:
    """Read one project price file; NTSG is converted from its EUR listing to USD."""
    with (DATA_DIR / filename).open(newline="") as file:
        prices = {
            date.fromisoformat(row["date"]): float(row["adjusted_price"])
            for row in csv.DictReader(file)
        }
    if filename == "NTSG.CSV":
        eurusd = read_prices("EURUSD.CSV")
        fx_dates = sorted(eurusd)
        latest_fx = {}
        position = -1
        for day in sorted(prices):
            while position + 1 < len(fx_dates) and fx_dates[position + 1] <= day:
                position += 1
            if position < 0:
                raise ValueError("EURUSD history starts after NTSG history.")
            latest_fx[day] = eurusd[fx_dates[position]]
        prices = {day: price * latest_fx[day] for day, price in prices.items()}
    return prices


def monthly_returns(prices: dict[date, float]) -> dict[tuple[int, int], float]:
    """Calculate returns between closed calendar months."""
    month_ends = {}
    for current_date, value in sorted(prices.items()):
        month_ends[(current_date.year, current_date.month)] = value
    months = sorted(month_ends)[:-1]
    return {
        current_month: month_ends[current_month] / month_ends[previous_month] - 1
        for previous_month, current_month in zip(months, months[1:])
    }


def correlation(left: list[float], right: list[float]) -> float:
    """Calculate Pearson correlation for two equally sized return lists."""
    left_mean = fmean(left)
    right_mean = fmean(right)
    covariance = sum(
        (left_value - left_mean) * (right_value - right_mean)
        for left_value, right_value in zip(left, right, strict=True)
    )
    left_variance = sum((value - left_mean) ** 2 for value in left)
    right_variance = sum((value - right_mean) ** 2 for value in right)
    if left_variance == 0 or right_variance == 0:
        return math.nan
    return covariance / math.sqrt(left_variance * right_variance)


def aligned_returns(
    series: dict[str, dict[tuple[int, int], float]],
) -> tuple[list[tuple[int, int]], dict[str, list[float]]]:
    """Align all return series to their common calendar-month sample."""
    common_months = sorted(set.intersection(*(set(values) for values in series.values())))
    return common_months, {
        name: [values[month] for month in common_months]
        for name, values in series.items()
    }


def write_panel(panel_name: str, files: dict[str, str]) -> tuple[tuple[int, int], tuple[int, int], int]:
    """Write one common-sample monthly correlation matrix."""
    returns = {name: monthly_returns(read_prices(filename)) for name, filename in files.items()}
    months, aligned = aligned_returns(returns)
    if len(months) < 2:
        raise ValueError(f"Panel {panel_name} has fewer than two common monthly returns.")

    names = list(files)
    with (OUTPUT_DIR / f"{panel_name}_correlations.csv").open("w", newline="") as file:
        writer = csv.writer(file, lineterminator="\n")
        writer.writerow(("instrument", *names))
        for left_name in names:
            writer.writerow(
                (
                    left_name,
                    *(f"{correlation(aligned[left_name], aligned[right_name]):.6f}" for right_name in names),
                )
            )
    return months[0], months[-1], len(months)


def validate_proxies() -> None:
    """Check output invariants and write overlap statistics against actual ETFs."""
    rows = []
    for name, (proxy_filename, actual_filename) in PROXY_VALIDATIONS.items():
        proxy_prices = read_prices(proxy_filename)
        proxy_dates = sorted(proxy_prices)
        first_return = proxy_prices[proxy_dates[1]] / proxy_prices[proxy_dates[0]] - 1
        if proxy_prices[proxy_dates[0]] != 100.0:
            raise ValueError(f"{name} proxy does not start at 100.")
        if any(value <= 0 for value in proxy_prices.values()):
            raise ValueError(f"{name} proxy contains a non-positive value.")
        if abs(first_return) >= 0.2:
            raise ValueError(f"{name} proxy has an implausible first return: {first_return:.2%}.")

        proxy_returns = monthly_returns(proxy_prices)
        actual_returns = monthly_returns(read_prices(actual_filename))
        months = sorted(proxy_returns.keys() & actual_returns.keys())
        proxy_values = [proxy_returns[month] for month in months]
        actual_values = [actual_returns[month] for month in months]
        differences = [
            proxy_value - actual_value
            for proxy_value, actual_value in zip(proxy_values, actual_values, strict=True)
        ]
        mean_difference = fmean(differences)
        tracking_error = math.sqrt(
            sum((difference - mean_difference) ** 2 for difference in differences) / (len(differences) - 1)
        ) * math.sqrt(12)
        rows.append(
            (
                name,
                len(months),
                f"{months[0][0]:04d}-{months[0][1]:02d}",
                f"{months[-1][0]:04d}-{months[-1][1]:02d}",
                f"{correlation(proxy_values, actual_values):.6f}",
                f"{mean_difference * 12:.6f}",
                f"{tracking_error:.6f}",
            )
        )

    with (OUTPUT_DIR / "proxy_validation.csv").open("w", newline="") as file:
        writer = csv.writer(file, lineterminator="\n")
        writer.writerow(
            (
                "instrument",
                "months",
                "start_month",
                "end_month",
                "correlation",
                "annualized_tracking_difference",
                "annualized_tracking_error",
            )
        )
        writer.writerows(rows)


def main() -> None:
    OUTPUT_DIR.mkdir(exist_ok=True)
    validate_proxies()
    summaries = []
    for panel_name, files in PANELS.items():
        start, end, months = write_panel(panel_name, files)
        summaries.append(
            (panel_name, f"{start[0]:04d}-{start[1]:02d}", f"{end[0]:04d}-{end[1]:02d}", months)
        )

    with (OUTPUT_DIR / "correlation_samples.csv").open("w", newline="") as file:
        writer = csv.writer(file, lineterminator="\n")
        writer.writerow(("panel", "start_month", "end_month", "monthly_returns"))
        writer.writerows(summaries)

    for panel_name, start, end, months in summaries:
        print(f"{panel_name}: {months} monthly returns, {start} to {end}")


if __name__ == "__main__":
    main()