# NTSG Historical Proxy

## Status

`data/NTSG_proxy.csv` is a transparent synthetic proxy, not the official WisdomTree Global Efficient Core Index or the NTSG ETF. It is suitable for exploratory long-history analysis and must be labelled as synthetic in every output.

## Official Strategy

The WisdomTree Global Efficient Core UCITS ETF tracks the WisdomTree Global Efficient Core Index (NTR), Bloomberg ticker `WTNTSGN`, in USD. The public product description states target exposures of 90% developed-market large-cap equities, 60% global government-bond futures, and approximately 10% cash collateral. It rebalances quarterly and has a 0.25% TER.

The issuer identifies US, German, UK, and Japanese government-bond futures as the current bond-futures markets. The equity sleeve also applies WisdomTree ESG exclusions.

## Proxy Inputs

| Component | Weight | Series | Treatment |
| --- | ---: | --- | --- |
| Developed-market equities | 90% | `data/URTH.CSV` | Add back URTH's 0.24% annual TER approximately. |
| Global bond futures | 60% notional | `data/BNDW.CSV` | Add back BNDW's 0.05% annual TER, then subtract synthetic cash returns to approximate a futures excess-return index. |
| USD cash collateral | 10% funded | `data/USD_CASH.CSV` | Build a cash index from FRED DGS3MO using the latest rate known at the start of each interval. |
| Proxy fee | -0.25% | NTSG TER | Deduct daily from net asset value. |

URTH is a practical developed-equity proxy. BNDW is a practical global-bond proxy, but it is not a basket of rolling sovereign-bond futures.

## Calculation

At the first available common observation, set the proxy NAV to 100. At each assumed quarterly rebalance, invest 90% of NAV in the equity proxy, retain 10% as cash collateral, and set bond-futures notional to 60% of NAV. Bond notional is not recorded as a funded asset.

Because BNDW is a funded total-return ETF, first approximate a bond-futures excess return:

$$
r_{b,t}^{excess}=\frac{1+r_{BNDW,t}}{1+r_{cash,t}}-1.
$$

Between rebalances, physical equity and cash units remain invested while changes in the bond excess-return index generate futures profit or loss that settles into cash. At target weights, the one-period approximation is:

$$
r_{proxy,t}\approx0.90r_{equity,t}+0.60r_{b,t}^{excess}+0.10r_{cash,t}-fee_t.
$$

The implementation tracks sleeve drift between quarterly resets and deducts the 0.25% annual fee multiplicatively from NAV.

## Limitations

- The proxy cannot reproduce the official ESG equity universe or its historical constituent weights.
- BNDW differs from the four-market government-futures basket in duration, country weights, credit exposure, currency exposure, and futures roll return.
- The cash series uses a USD Treasury rate rather than the index's multi-currency collateral basket.
- TER add-backs are approximations because ETF expense accrual and tracking differences are not directly observable.
- Quarterly resets are a proxy assumption until the exact official index effective dates are encoded.
- The proxy begins at the first common date of URTH and BNDW, not at the index inception date.

## Validation

From December 2024 through September 2026, 22 overlapping monthly returns have 0.963 correlation, 0.48% annualized proxy-minus-fund return difference, and 3.41% annualized tracking error. This is a short validation sample and the proxy weights must not be tuned to it.

## Extended Proxy

`data/NTSG_proxy_extended.csv` extends the synthetic history back to the first common observation of its ETF inputs. It is deliberately separate from `NTSG_proxy.csv` because its inputs are less faithful to the official index.

| Exposure | Extended input | Overall target weight |
| --- | --- | ---: |
| US developed equities | SPY | 63.0% |
| Developed equities excluding North America | EFA | 24.3% |
| Canadian equities | EWC | 2.7% |
| US government bonds | IEF | 30.0% |
| International government bonds | BWX | 30.0% |
| USD cash | USD_CASH | 10.0% |

The equity weights approximate a 70% US, 27% developed ex-US, and 3% Canadian developed-market sleeve. The bond weights use an equal US/international split because the public NTSG materials identify the four government-futures markets but do not publish their historical target weights.

The extended proxy treats SPY, EFA, and EWC as funded equity holdings. It converts IEF and BWX total returns to excess returns over synthetic cash before applying their 30% futures notionals. It applies the same assumed quarterly reset and deducts the 0.25% NTSG TER. It must be used only for sensitivity analysis, not spliced silently into the higher-fidelity proxy or presented as official NTSG performance.