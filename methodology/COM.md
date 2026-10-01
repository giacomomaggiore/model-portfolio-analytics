# COM Historical Index Proxy

## Status

`data/COM_proxy.csv` is an index-based historical proxy for COM, not reconstructed
fund NAV. It uses the issuer-published Auspice Broad Commodity Total Return Index
(`ABCTRI`) and deducts COM's 0.70% annual expense ratio. Use actual `data/COM.CSV`
whenever the requested period begins after the fund's 2017 inception.

## Official Strategy

COM is actively managed and seeks returns, before fees and expenses, that exceed
the Auspice Broad Commodity Index over a complete market cycle. The underlying
Auspice strategy is systematic and tactical rather than a static commodity basket:

- It trades a diversified set of exchange-traded energy, metal, and agricultural
	futures.
- Each commodity can be long or flat. The strategy does not need to keep the
	whole basket invested.
- Momentum and term structure determine participation. Term structure is the
	shape of futures prices across maturities. Contango can create negative roll
	return, while backwardation can create positive roll return; neither outcome
	is guaranteed.
- Position weights and rebalancing use volatility-based risk management.
- Contract selection seeks the best expected roll return along each forward
	curve, accounting for contango and backwardation.

The public description does not disclose the full production formulas, signal
lookbacks, risk budgets, contract eligibility rules, or roll calendar. Those rules
must not be reverse-engineered from COM's realized returns.

## Excess Return, Collateral, and Fees

Auspice publishes two versions:

| Series | Contents |
| --- | --- |
| `ABCERI` | Futures price change plus roll return; no collateral interest |
| `ABCTRI` | `ABCERI` plus interest on collateral such as Treasury bills |

COM references the excess-return index but also earns interest on its U.S.
collateral. `ABCTRI` is therefore the closest published all-in proxy available.
It is preferable to adding a separate synthetic cash series to `ABCERI`, because
the official total-return series already performs that calculation consistently.

The project compounds the published index return and then deducts COM's fee over
calendar days:

$$
V_t=V_{t-1}\frac{ABCTRI_t}{ABCTRI_{t-1}}
\left(1-\frac{0.0070}{365}\right)^{d_t}.
$$

The series is normalized to 100 on 2000-01-01. No source ETF fee is added back,
because `ABCTRI` is an index rather than a fund.

## Historical Boundary

Auspice states that performance before 2010-09-30 is simulated and hypothetical;
the live third-party-published history starts after that date. Consequently:

- 2000-01-01 through 2010-09-29 is a backtested index proxy.
- 2010-09-30 onward is a live index proxy.
- 2017 onward should use actual COM returns for fund-level analysis.

Even after 2017, index and fund returns can differ through active management,
implementation, collateral instruments, transaction costs, tax constraints,
tracking, and the fund fee.

## Validation

From April 2017 through August 2026, 113 closed-month returns have 0.989
correlation, -0.37% annualized mean proxy-minus-fund return, and 1.34% annualized
tracking error.
The strong fit supports the index as a sensitivity backfill, but it does not turn
simulated pre-2010 index history into investable COM performance.

## Sources

- [Auspice Broad Commodity Index](https://www.auspicecapital.com/auspice-broad-commodity)
- Auspice `AuspiceIndicesData.xlsx`, downloaded by
	`helpers/build_strategy_proxies.py`
- [Direxion COM product page](https://www.direxion.com/product/auspice-broad-commodity-strategy-etf)