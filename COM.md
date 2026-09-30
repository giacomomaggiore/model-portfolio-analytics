# COM Historical Proxy

COM tracks the Auspice Broad Commodity Strategy Index, a diversified commodity-futures strategy with a trend-driven long-or-cash overlay. The public descriptions do not disclose enough historical contract, roll, and signal detail to recreate the index exactly.

`data/COM_proxy.csv` is therefore a transparent substitute: it uses DBC as the broad commodity basket, applies an assumed monthly 252-trading-day moving-average signal, holds commodities when the prior close is at or above the moving average, and otherwise holds synthetic USD cash. DBC's 0.85% TER is removed multiplicatively and COM's 0.70% TER is deducted daily.

This proxy makes one aggregate all-in or all-out decision. It does not replicate Auspice's individual commodity signals, commodity weights, futures rolls, or exact cash allocation. The lookback and monthly decision schedule are model assumptions, not disclosed issuer parameters.

From April 2017 through September 2026, 114 overlapping monthly returns have 0.738 correlation, 3.16% annualized proxy-minus-fund return difference, and 9.05% annualized tracking error. Label it as a generic commodity-trend style proxy, not a COM reconstruction or backfill.