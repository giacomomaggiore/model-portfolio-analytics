# GDE Historical Proxy

GDE is actively managed and seeks exposure to US large-cap equities and US-listed gold futures. The public fund description and the portfolio article identify approximate 90% equity and 90% gold target exposures, funded with a cash collateral sleeve; the fund's net expense ratio is 0.20%. Actual exposures can drift from these approximate targets.

`data/GDE_proxy.csv` assumes quarterly resets. It invests 90% of NAV in SPY, retains 10% in synthetic USD cash, and applies a 90% gold notional whose profit and loss settles into cash. Gold notional is not booked as another funded asset. The implementation approximately removes the input ETF fee drags and deducts GDE's 0.20% annual fee multiplicatively.

GLD is physically backed and is used as an approximation of gold-futures excess returns. It differs from rolling gold futures through roll return, contract selection, collateral, and implementation. Quarterly resetting is a modeling assumption rather than a claim that the active fund follows a published quarterly index rule.

From April 2022 through September 2026, 54 overlapping monthly returns have 0.988 correlation, 4.78% annualized proxy-minus-fund return difference, and 3.48% annualized tracking error. The high correlation supports exposure analysis, but the return difference prevents treating the series as reconstructed GDE performance.