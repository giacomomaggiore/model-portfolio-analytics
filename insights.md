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

- Result: `GDE_proxy.csv` provides a 90% SPY, 90% GLD, and 10% USD-cash exposure from 2004-11-18; `COM_proxy.csv` provides a DBC-based monthly long-or-cash trend proxy from 2007-02-07; and `DBMF_proxy.csv` uses WTMF as a managed-futures proxy from 2011-01-05.
- Decision: Use `PPUT.CSV`, the Cboe S&P 500 5% Put Protection Index, as a long-run protective-put benchmark from 1986-06-30 instead of fabricating a TAIL reconstruction.
- Limitation: COM's sector-level signals and DBMF's Dynamic Beta Engine are not publicly reproducible. GLD differs from GDE's gold-futures implementation. PPUT owns equities plus a monthly 5% out-of-the-money put, so it is not equivalent to TAIL's Treasury-backed deep-tail put ladder.

## 2026-09-29 - Proxy accounting correction and validation

- Correction: Replaced gross-notional asset summation in the NTSG and GDE proxies with funded physical sleeves, cash collateral, and separately tracked futures profit and loss. The former method incorrectly multiplied NAV by gross exposure at quarterly resets.
- Correction: Cash now accrues at the latest yield known at the start of each interval. ETF fee add-backs and DBMF fee substitution now compound multiplicatively.
- Result: Corrected terminal proxy levels are 227.98 for NTSG from September 2018, 471.81 for extended NTSG from October 2007, and 5,967.10 for GDE from November 2004. All begin at 100 without artificial first-period jumps.
- Validation: Monthly proxy/fund correlations are 0.963 for NTSG, 0.988 for GDE, 0.738 for COM, and 0.273 for the WTMF-based DBMF peer. The low DBMF result rejects WTMF as a historical DBMF backfill.
- Decision: Keep actual ETF, synthetic sensitivity, and underlying-exposure correlations in separate common-sample panels. Never use PPUT as TAIL inside the model portfolio; it remains a separately labelled protective-put benchmark.
