"""Download adjusted-price histories for the portfolio and benchmarks."""

import csv
import json
from datetime import UTC, datetime
from pathlib import Path
from urllib.parse import urlencode
from urllib.error import HTTPError, URLError
from urllib.request import Request, urlopen


DATA_DIR = Path(__file__).resolve().parent.parent / "data"
YAHOO_CHART_URL = "https://query1.finance.yahoo.com/v8/finance/chart/{ticker}"

INSTRUMENTS = (
    ("NTSG", "NTSG.L", "WisdomTree Global Efficient Core UCITS ETF - USD Acc", 0.0025, "USD"),
    ("COM", "COM", "Direxion Auspice Broad Commodity Strategy ETF", 0.0070, "USD"),
    ("DBMF", "DBMF", "iMGP DBi Managed Futures Strategy ETF", 0.0085, "USD"),
    ("GDE", "GDE", "WisdomTree Efficient Gold Plus Equity Strategy Fund", 0.0020, "USD"),
    ("TAIL", "TAIL", "Cambria Tail Risk ETF", 0.0060, "USD"),
    ("VT", "VT", "Vanguard Total World Stock ETF", 0.0006, "USD"),
    ("BNDW", "BNDW", "Vanguard Total World Bond ETF", 0.0005, "USD"),
    ("PDBC", "PDBC", "Invesco Optimum Yield Diversified Commodity Strategy No K-1 ETF", 0.0059, "USD"),
    ("WTMF", "WTMF", "WisdomTree Managed Futures Strategy Fund", 0.0065, "USD"),
    ("SPY", "SPY", "SPDR S&P 500 ETF Trust", 0.000945, "USD"),
    ("GLD", "GLD", "SPDR Gold Shares", 0.0040, "USD"),
    ("URTH", "URTH", "iShares MSCI World ETF", 0.0024, "USD"),
    ("EFA", "EFA", "iShares MSCI EAFE ETF", 0.0032, "USD"),
    ("EWC", "EWC", "iShares MSCI Canada ETF", 0.0050, "USD"),
    ("IEF", "IEF", "iShares 7-10 Year Treasury Bond ETF", 0.0015, "USD"),
    ("BWX", "BWX", "SPDR Bloomberg International Treasury Bond ETF", 0.0035, "USD"),
    ("DBC", "DBC", "Invesco DB Commodity Index Tracking Fund", 0.0085, "USD"),
)

DERIVED_INSTRUMENTS = (
    ("USD_CASH", "Synthetic USD cash index from FRED DGS3MO", 0.0, "USD"),
    ("NTSG_PROXY", "Synthetic WisdomTree Global Efficient Core proxy", 0.0025, "USD"),
    ("NTSG_PROXY_EXTENDED", "Extended synthetic WisdomTree Global Efficient Core proxy", 0.0025, "USD"),
    ("USD_CASH_LONG", "Long synthetic USD cash index from FRED DGS3MO", 0.0, "USD"),
    ("COM_PROXY", "Synthetic broad commodity trend proxy", 0.0070, "USD"),
    ("DBMF_PROXY", "WTMF managed-futures peer with DBMF fee assumption", 0.0085, "USD"),
    ("GDE_PROXY", "Synthetic WisdomTree Efficient Gold Plus Equity proxy", 0.0020, "USD"),
    ("PPUT", "Cboe S&P 500 5% Put Protection Index", 0.0, "USD"),
)


def download_adjusted_prices(ticker: str) -> list[tuple[str, float]]:
    """Return Yahoo Finance daily adjusted closes for one ticker."""
    query = urlencode({"period1": 0, "period2": int(datetime.now(UTC).timestamp()), "interval": "1d"})
    request = Request(
        f"{YAHOO_CHART_URL.format(ticker=ticker)}?{query}",
        headers={"User-Agent": "model-portfolio-backtest/1.0"},
    )
    with urlopen(request, timeout=30) as response:
        payload = json.load(response)

    result = payload["chart"]["result"][0]
    timestamps = result["timestamp"]
    adjusted_prices = result["indicators"]["adjclose"][0]["adjclose"]
    rows = []
    for timestamp, adjusted_price in zip(timestamps, adjusted_prices, strict=True):
        if adjusted_price is not None:
            date = datetime.fromtimestamp(timestamp, UTC).date().isoformat()
            rows.append((date, adjusted_price))
    return rows


def write_price_file(ticker: str, rows: list[tuple[str, float]]) -> None:
    """Write a price history using the project's two-column CSV contract."""
    path = DATA_DIR / f"{ticker}.CSV"
    with path.open("w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(("date", "adjusted_price"))
        writer.writerows(rows)


def write_metadata() -> None:
    """Write the instrument metadata used by the analysis."""
    path = DATA_DIR / "metadata.csv"
    with path.open("w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(("ticker", "asset_name", "ter", "currency"))
        writer.writerows((ticker, asset_name, ter, currency) for ticker, _, asset_name, ter, currency in INSTRUMENTS)
        writer.writerows(DERIVED_INSTRUMENTS)


def main() -> None:
    DATA_DIR.mkdir(exist_ok=True)
    write_metadata()
    failed_tickers = []
    for ticker, source_ticker, _, _, _ in INSTRUMENTS:
        try:
            rows = download_adjusted_prices(source_ticker)
        except (HTTPError, URLError, KeyError, IndexError) as error:
            failed_tickers.append(ticker)
            print(f"Could not download {ticker} ({source_ticker}): {error}")
            continue

        write_price_file(ticker, rows)
        print(f"Downloaded {ticker}: {len(rows)} rows")

    if failed_tickers:
        raise SystemExit(f"Download failed for: {', '.join(failed_tickers)}")


if __name__ == "__main__":
    main()