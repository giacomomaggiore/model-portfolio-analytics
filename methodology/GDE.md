# GDE Historical Exposure Proxy

## Status

`data/GDE_proxy.csv` is a transparent 90/90 exposure model, not reconstructed GDE
NAV. GDE is actively managed, so use actual `data/GDE.CSV` from its 2022-03-17
inception and use the proxy only for longer-run sensitivity analysis.

## Official Strategy

GDE seeks total return through U.S. large-cap equities and U.S.-listed gold
futures, held directly or through a wholly owned subsidiary. WisdomTree describes
the design as approximately 90% equity exposure plus 90% gold-futures notional,
or about 180% gross market exposure for each dollar of NAV. The current net
expense ratio is 0.20%.

The equity sleeve is a market-cap-oriented basket of U.S. large-cap securities.
Gold exposure is obtained with leveraged futures rather than a funded physical
gold holding. The remaining assets and margin collateral can earn income. Because
the fund is active, 90/90 is an exposure objective rather than a daily invariant;
live holdings on 2026-09-28 were about 86.5% equities and 87.7% gold futures.

Public materials do not define a mechanical rebalance calendar, exposure band,
gold contract tenor, or roll rule sufficient for exact reconstruction.

## Project Construction

The proxy uses:

| Component | Target | Input | Treatment |
| --- | ---: | --- | --- |
| U.S. large-cap equities | 90% funded | `SPY.CSV` | Add back SPY's 0.0945% fee approximately |
| Gold | 90% notional | `GLD.CSV` | Add back GLD's 0.40% fee and use price changes as a gold-return approximation |
| USD cash | 10% funded | `USD_CASH_LONG.CSV` | FRED DGS3MO cash index |
| GDE fee | -0.20% | Fund TER | Deduct over calendar days |

At a reset, 90% of NAV buys the equity proxy and 10% remains in cash. The gold
position is a notional overlay. Its change is settled into cash rather than booked
as another funded asset:

$$
NAV_t=E_t+C_t+N_{gold,t-1}
\left(\frac{G_t}{G_{t-1}}-1\right)-fee_t.
$$

The code resets on calendar-quarter boundaries, effectively at the last available
business day of March, June, September, and December. This is a project assumption,
not a published GDE rule.

## Gold Proxy Limitation

GLD is physically backed. Removing its stated fee approximates physical gold,
not a gold-futures excess-return index. GDE's futures return also reflects contract
selection, term structure, roll timing, margin, and collateral. A licensed gold
futures index with documented rolls would improve that sleeve, but it would still
not reproduce active GDE positions.

## Validation

From April 2022 through August 2026, 53 closed-month returns have 0.987
correlation, 0.93% annualized mean proxy-minus-fund return, and 3.56% annualized
tracking error. High correlation supports broad exposure analysis, but the proxy
still cannot be presented as reconstructed fund performance.

## Sources

- [WisdomTree GDE product page](https://www.wisdomtree.com/us/etfs/capital-efficient/gde)
- [WisdomTree capital-efficient strategies](https://www.wisdomtree.com/us/strategies/capital-efficient-etfs)