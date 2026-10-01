# Insights

Record material assumptions, data decisions, results, and their interpretations here as soon as they are established.

## 2026-09-29 - Historical data downloaded

- Decision: Use Yahoo Finance adjusted-close history for NTSG, COM, DBMF, GDE, TAIL, VT, and BNDW. The generated metadata is in `data/metadata.csv`.
- Finding: The UCITS version of NTSG must be requested as `NTSG.L` from Yahoo Finance, while its project data file remains `data/NTSG.CSV`.
- Result: The adjusted-price CSVs downloaded successfully. Their history ranges from 476 observations for NTSG to 4,593 for VT.
- Limitation: Different inception dates constrain any actual-ETF portfolio backtest to the latest common history. Earlier analysis requires clearly labeled synthetic reconstructions.

## 2026-09-29 - Broad correlation proxy set

- Decision: Use VT and BNDW for global equities and global bonds; PDBC for broad commodities; WTMF for managed futures; SPY for US large-cap equities; GLD for gold; and TAIL for the tail-risk strategy.
- Result: Adjusted-price histories for PDBC, WTMF, SPY, and GLD were downloaded and added to `data/metadata.csv`.
- Limitation: These proxies describe asset-class relationships and do not recreate the holdings, futures implementation, or risk profile of the portfolio ETFs. The correlation sample is limited by NTSG's November 2024 inception when using actual holdings and proxies together.

## 2026-09-29 - Synthetic NTSG proxy built

- Decision: Build `data/NTSG_proxy.csv` from 90% URTH developed-market equities, 60% BNDW global bonds, and 10% synthetic USD cash; reset target exposures quarterly and deduct NTSG's 0.25% TER.
- Result: The proxy and `data/USD_CASH.CSV` both contain 2,026 daily observations from 2018-09-06 to 2026-09-29.
- Limitation: The proxy substitutes broad bond exposure for the official basket of US, German, UK, and Japanese government-bond futures, and it uses USD cash instead of multi-currency collateral. It is therefore a synthetic analysis series, not official NTSG or index performance.
- Follow-up: Compare monthly proxy and actual NTSG returns from November 2024 onward before using the proxy in a portfolio backtest.

## 2026-09-29 - Extended NTSG proxy

- Decision: Create `data/NTSG_proxy_extended.csv` separately from the baseline proxy, using SPY, EFA, and EWC for developed equities plus IEF and BWX for government bonds.
- Result: The extended proxy has 4,771 daily observations from 2007-10-11 to 2026-09-29, compared with 2,026 observations from 2018-09-06 for `NTSG_proxy.csv`.
- Limitation: The extended series approximates the public NTSG exposures with fixed regional ETF and US/international bond weights. It is lower fidelity than the baseline proxy and must be used only for sensitivity analysis, never silently spliced into it.

## 2026-09-29 - Strategy proxy series

- Result: `GDE_proxy.csv` provides a 90% SPY, 90% GLD-return, and 10% USD-cash exposure from 2004-11-18; `COM_proxy.csv` uses the published Auspice ABCTRI series from 2000-01-01; and `DBMF_proxy.csv` is a fee-adjusted WTMF peer from 2011-01-05.
- Decision: Use `PPUT.CSV`, the Cboe S&P 500 5% Put Protection Index, as a long-run protective-put benchmark from 1986-06-30 instead of fabricating a TAIL reconstruction.
- Limitation: COM's sector-level signals and DBMF's Dynamic Beta Engine are not publicly reproducible. GLD differs from GDE's gold-futures implementation. PPUT owns equities plus a monthly 5% out-of-the-money put, so it is not equivalent to TAIL's Treasury-backed deep-tail put ladder.

## 2026-09-29 - Proxy accounting correction and validation

- Correction: Replaced gross-notional asset summation in the NTSG and GDE proxies with funded physical sleeves, cash collateral, and separately tracked futures profit and loss. The former method incorrectly multiplied NAV by gross exposure at quarterly resets.
- Correction: Cash now accrues at the latest yield known at the start of each interval. ETF fee add-backs and DBMF fee substitution now compound multiplicatively.
- Result: Corrected terminal proxy levels are 227.98 for NTSG from September 2018, 471.81 for extended NTSG from October 2007, and 5,967.10 for GDE from November 2004. All begin at 100 without artificial first-period jumps.
- Validation: These figures were superseded by the 2026-09-30 closed-month audit below.
- Decision: Keep actual ETF, synthetic sensitivity, and underlying-exposure correlations in separate common-sample panels. Never use PPUT as TAIL inside the model portfolio; it remains a separately labelled protective-put benchmark.

## 2026-09-30 - Methodology audit and proxy upgrades

- NTSG correction: The official index resets on the last business day of February, May, August, and November, not calendar-quarter ends, and also resets if equity or bond exposure differs from target by more than 5 percentage points. Both NTSG proxies now implement those rules. Closed-month validation through August 2026 is recorded below.
- COM correction: Replaced the DBC 252-day moving-average style model with Auspice's published daily collateralized `ABCTRI` levels, less COM's 0.70% fee. The new series has 9,769 observations from 2000-01-01 through 2026-09-29 and ends at 783.37. History before 2010-09-30 is issuer-labelled simulated index history.
- COM validation: Closed-month results through August 2026 are 0.989 correlation, -0.37% annualized mean active return, and 1.34% tracking error against COM. This is materially more faithful than the rejected DBC style model.
- DBMF decision: WTMF and CTA are independent managed-futures systems, not Dynamic Beta Engine reconstructions. Keep WTMF only as a fee-adjusted peer; its 0.279 closed-month correlation rejects it as a backfill. A licensed SG CTA series would be a benchmark, not DBMF performance.
- TAIL decision: Cambria discloses roughly 80%-95% in approximately 10-year Treasuries, 1-16 month SPX puts typically 5%-15% out of the money, roughly 1% of AUM spent monthly, and volatility-sensitive notional sizing. These ranges are insufficient for reconstruction. Keep PPUT only as a separate protective-put benchmark.
- GDE decision: Retain the 90% SPY, 90% GLD-return, 10% cash exposure model as a sensitivity proxy. GDE is active, live exposures drift, and no complete public rebalance or gold-futures roll rule was found.
- Limitation: Source files include a partial September 2026. Correlation and validation outputs now exclude every terminal month unless a later observation proves that month closed.

## 2026-09-30 - MSCI World price-index correlation benchmark

- Decision: Replace VT with Yahoo Finance symbol `^990100-USD-STRD`, stored as `data/MSCI_WORLD_USD.CSV`, for all rolling and monthly correlation panels. The downloaded series contains 14,017 daily observations from 1972-01-03 through 2026-09-30.
- Source: Yahoo Finance chart API, downloaded 2026-09-30.
- Limitation: This is the MSCI World standard price index, not MSCI World Net Total Return. It excludes dividends, emerging markets, and small caps; it is used deliberately to provide a much longer developed-market equity correlation benchmark.

## 2026-10-01 - Inflation correlation data

- Data: Added `data/CPIAUCSL.CSV` from the FRED Consumer Price Index for All Urban Consumers (CPIAUCSL), downloaded 2026-10-01. It contains 955 monthly index observations from 1947-01-01 through 2026-08-01.
- Method: Inflation is the year-over-year percent change in the monthly CPI index. Rolling correlations use 36 monthly observations between that rate and each asset's month-end total return.
- Series: The panels compare inflation with actual WTMF for managed futures, BWX for the longest available global-government-bond proxy, and the fee-adjusted Auspice ABCTRI proxy for commodities.
- Limitation: A correlation between monthly return and year-over-year CPI is descriptive and mixes a one-month asset-return horizon with a trailing 12-month price-change measure; it is not a causal estimate of inflation hedging.

## 2026-09-30 - Daily USD portfolio backtests

- Data decision: Replaced the NTSG source with the EUR-traded `NTSG.DE` listing and added Yahoo Finance `EURUSD=X`, stored as `data/EURUSD.CSV`. Daily NTSG USD values equal the EUR adjusted price times USD per EUR. From 2024-11-13 through 2026-09-30, NTSG returned 18.99% in EUR and 27.03% in USD.
- Cash-rate decision: Added `data/USD_CASH_EFFR.CSV`, a USD cash index compounded across each calendar gap at the prior observed FRED Effective Federal Funds Rate on an ACT/360 basis. The data is used as the daily risk-free return in Sharpe ratios.
- Method: All portfolio legs use daily adjusted prices, target capital weights of 60% NTSG, 10% COM, 15% DBMF, 10% GDE, and 5% TAIL, with month-end rebalancing, zero transaction costs, and zero capital-gains taxes. The 60/40 benchmark is 60% VT and 40% BNDW, rebalanced on the same schedule; VT is the 100% equity benchmark.
- Actual ETF result: On the common 2024-11-13 to 2026-09-30 sample, the model CAGR was 15.70%, maximum drawdown -10.68%, annualized volatility 10.86%, and EFFR-based Sharpe 1.02. The 60/40 benchmark had 11.28% CAGR and 0.72 Sharpe; VT had 17.91% CAGR and 0.87 Sharpe.
- Superseded result: The original proxy-extended run backfilled DBMF with WTMF and began in 2018. The audit rejected that substitution; current results are recorded below.

## 2026-09-30 - Audit: GDE proxy fix, NTSG validation, notebook rebuild

- GDE correction: `GDE_proxy.csv` used GLD *spot* returns as the gold-futures excess return and never subtracted cash, overstating the proxy by about 0.9 x the cash rate per year. After subtracting cash (`excess_return_index`), closed-month validation through August 2026 has +0.93% annualized proxy-minus-fund return, 0.987 correlation, and 3.56% tracking error. The terminal level fell from 5,967 to 4,181 (2004-11-18 start). `USD_CASH_LONG.CSV` was rebuilt from FRED DGS3MO (downloaded 2026-09-30) to cover 2026-09-30.
- NTSG validation correction: `NTSG.CSV` is the EUR-listed line, so validation must convert it to USD with EURUSD first. Closed-month validation through August 2026 has 0.932 correlation, +0.73% annualized tracking difference, and 4.33% tracking error over 21 months.
- Timing caveat: daily NTSG (Xetra close, EURUSD 24:00 London close) versus US-listed assets is non-synchronous. Daily correlation of actual NTSG with the USD proxy is about 0.27 and weekly about 0.81, so daily volatility, Sharpe and drawdown of the actual-ETF backtest are approximate.
- Notebook change: the synthetic-sensitivity backtest does not backfill DBMF or TAIL and uses actual COM because COM predates DBMF. The window starts at DBMF inception, 2019-05-08. Results (USD, monthly rebalancing): model CAGR 11.60%, Sharpe 0.70, max drawdown -22.4%; 60/40 CAGR 8.34%, Sharpe 0.50; VT CAGR 13.10%, Sharpe 0.60. Only NTSG and GDE contain synthetic pre-inception segments.
- Metrics: CAGR uses the full elapsed period. Volatility, Sharpe, and Sortino use the observed sample frequency rather than assuming 252 observations per year. Cumulative return, Calmar, complete-calendar-year return, and one-year rolling-return quantiles are reported.
- Correlation validation: Terminal months are excluded. Through August 2026, proxy/fund correlations are 0.932 for NTSG, 0.987 for GDE, 0.989 for COM, and 0.279 for the WTMF-based DBMF peer.
- Not yet done: EUR and CHF periodic-return reporting and TER-consistent cash rates across proxies (DGS3MO in proxies, EFFR in Sharpe).
