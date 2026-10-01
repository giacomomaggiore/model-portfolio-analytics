# TAIL Methodology and Benchmark Decision

## Status

No synthetic `TAIL_proxy.csv` is created. Use actual `data/TAIL.CSV` from the
fund's 2017-04-06 inception. A defensible reconstruction would require daily SPX
option surfaces, Treasury holdings, trade records, and Cambria's complete sizing
rules; adjusted prices alone are insufficient.

## Disclosed Fund Construction

TAIL is an actively managed risk-mitigation fund with two unlike sleeves:

| Sleeve | Public guidance |
| --- | --- |
| U.S. government bonds | Approximately 80%-95% of NAV, typically around 10-year maturity |
| Long SPX puts | A ladder with roughly 1-16 months to expiry and strikes typically 5%-15% out of the money |

Cambria's FAQ says the fund targets spending roughly 1% of AUM on puts each
month. It normally sells options before expiry to avoid the fastest final-months
time decay. Notional exposure is adaptive: it is reduced when volatility and
option premiums are high and increased when volatility is low. The fund charges
0.60% annually.

These are ranges and portfolio guidelines, not a complete mechanical index rule.
The exact contracts, trade dates, strike interpolation, sale rules, volatility
measure, sizing function, and Treasury issues remain discretionary or undisclosed.
For example, the live portfolio on 2026-09-29 held about 91.8% in a May 2035
Treasury and several SPX puts with different 2026-2027 expiries and strikes.

## Why PPUT Is Not a Reconstruction

`data/PPUT.CSV` is the Cboe S&P 500 5% Put Protection Index. PPUT owns an S&P
500 equity portfolio and buys a one-month 5% out-of-the-money SPX put, normally
rolling monthly. TAIL instead owns mostly Treasuries and a multi-expiry,
volatility-sized put ladder.

Substituting PPUT for TAIL would add a funded equity exposure that TAIL does not
have and would materially change ordinary-market beta, carry, duration, crash
convexity, and option decay. PPUT is retained only as a separately labelled
protective-put benchmark in the synthetic correlation panel.

## Reconstruction Requirements

A future TAIL reconstruction would need, at minimum:

1. Point-in-time SPX option bid/ask surfaces and settlement conventions.
2. Exact monthly premium budget and volatility-to-notional sizing function.
3. Contract selection, strike, expiry, sale, and replacement rules.
4. Historical Treasury security selection, coupon income, and rebalancing.
5. Transaction costs, option spreads, exercise/settlement, and the 0.60% fee.

Without those inputs, a fitted option model would be an invented tail strategy,
not historical TAIL.

## Sources

- [Cambria TAIL product page](https://www.cambriafunds.com/tail)
- [Cambria TAIL FAQ](https://www.cambriafunds.com/assets/docs/Cambria_Tail_FAQ.pdf)
- Cboe `PPUT_History.csv`, downloaded by `helpers/build_strategy_proxies.py`