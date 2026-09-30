# DBMF Historical Proxy

DBMF is actively managed through DBi's Dynamic Beta Engine, which estimates managed-futures hedge-fund factor exposures and expresses them through liquid futures. Its estimation window, input manager universe, portfolio constraints, and daily target exposures are not publicly sufficient for a reconstruction.

`data/DBMF_proxy.csv` uses WTMF, a diversified systematic managed-futures ETF, as an investable peer. The construction removes WTMF's 0.65% TER and deducts DBMF's 0.85% TER multiplicatively through time.

WTMF is not a DBMF reconstruction. Unlike DBMF's hedge-fund factor-replication process, it follows its own systematic futures methodology. From June 2019 through September 2026, 88 overlapping monthly returns have only 0.273 correlation, -3.96% annualized peer-minus-DBMF return difference, and 11.33% annualized tracking error.

These results reject WTMF as a historical DBMF backfill. Use it only as a separately labelled investable managed-futures peer. A licensed managed-futures manager index may be a better strategy benchmark, but it would remain non-investable and would not reconstruct DBMF.