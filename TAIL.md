# TAIL Strategy Benchmark

TAIL holds US Treasuries and a ladder of out-of-the-money S&P 500 put options. Its option strikes, maturities, sizing, and purchases can respond to market conditions and volatility, so adjusted-price inputs cannot reproduce the fund without a complete historical option surface and its active rules.

No synthetic `TAIL_proxy.csv` is created because it would imply unsupported precision. Use actual `data/TAIL.CSV` from fund inception for ETF results.

For a long-run protective-put strategy benchmark, `data/PPUT.CSV` contains the Cboe S&P 500 5% Put Protection Index. PPUT holds S&P 500 stocks and a one-month 5% out-of-the-money SPX put, typically rebalanced on the third Friday of each month. It reflects a protective-put strategy, not TAIL's Treasury-backed option ladder.

Never substitute PPUT for TAIL inside the model portfolio: doing so would introduce a funded S&P 500 allocation where TAIL primarily holds Treasuries. PPUT appears only as a separately labelled benchmark in the synthetic correlation panel.