# Market-Microstructure Statistical Arbitrage (Pairs / Multi-asset)

Build a robust market-microstructure aware statistical-arbitrage system that discovers, backtests, and simulates execution for pair and small-basket mean-reversion strategies with realistic transaction costs and slippage.

## Goals
* Find cointegrated pairs / baskets and build trading signals (stat-arb).

* Backtest with realistic execution model (latency, spread, slippage, fees).

* Evaluate risk-adjusted returns, stress scenarios, and portfolio-level exposure.

* Provide an interactive dashboard and production-ready code + Docker.

## Data
* Historical minute/1-min OHLCV for equities / ETFs via Yahoo/AlphaVantage/IEX/Polygon (or LOBSTER for limit order book if you want deeper microstructure).

* Trade and quote (TAQ) or LOBSTER if available for advanced execution simulation (optional).

* Alternative: use cryptomarkets (Binance via CCXT) for free high-frequency data.

## Methods / Models
* Pair selection: unit-root / Engle-Granger cointegration, Johansen for multi-asset, distance / Mahalanobis clustering, PCA for factor neutralization.

* Signal generation: z-score on spread, Kalman filter (dynamic hedge ratio), mean-reversion entry/exit thresholds.

* Risk controls: position sizing via Kelly/vol targeting, max exposure, stop-loss, friction-aware position limits.

* Execution simulation: spread model, percent-of-ADTV limits, fixed/variable slippage model, limit vs market fills, latency modeling.

* Portfolio construction: mean-variance or risk-parity across pairs; capital allocation rules.

## Implementation plan (step-by-step)
1. Data ingestion: write ETL to fetch and store OHLCV (parquet), align timestamps, handle corporate actions.

2. Exploratory analysis: correlation matrices, stationarity tests, cointegration candidate list.

3. Signal module: implement static hedge ratio and Kalman filter versions; generate signals & PnL pipeline.

4. Execution simulator: microstructure model with configurable spread/slippage & fill rules.

5. Backtester: vectorized backtest with transaction costs, daily/ intraday simulation, walk-forward testing.

6. Risk & analytics: Sharpe, Sortino, max drawdown, Calmar, turnover, hit rate, long/short exposure.

7. Dashboard: Streamlit/Plotly showing signals, live PnL, heatmaps, trade logs.

Packaging: Dockerfile, reproducible notebook, README, unit tests.

## Tech stack
* Python, pandas, NumPy, statsmodels, scikit-learn

* backtesting.py or custom vectorized backtester; optional Backtrader/zipline

* Kalman filter: pykalman or custom

* Visualization: Streamlit, Plotly

* GitHub, Docker

## Evaluation / metrics to show on resume
* Annualized return, annualized volatility, Sharpe ratio (e.g., “Sharpe 1.35 after transaction costs”)

* Max drawdown, CAGR, turnover, daily hit rate

* Out-of-sample performance (e.g., “OOS Sharpe 1.12 over 12 months; bootstrap p-value < 0.05”)

* Trade distribution, average slippage in bps

## 1. Repository Structure
```
market_microstructure_stat_arb/
│
├── data/                      # Raw & processed market data
├── notebooks/                 # Jupyter EDA & prototype models
│   ├── 01_eda.ipynb
│   ├── 02_cointegration_tests.ipynb
│   ├── 03_signal_backtest.ipynb
│
├── src/
│   ├── __init__.py
│   ├── data_loader.py         # Fetch & preprocess data
│   ├── cointegration.py       # Pair selection
│   ├── signal_generation.py   # Z-score, Kalman filter, thresholds
│   ├── backtester.py          # Vectorized backtesting w/ costs
│   ├── execution.py           # Slippage & fill simulation
│   ├── risk.py                # Sharpe, drawdown, volatility
│   ├── dashboard.py           # Streamlit app
│
├── requirements.txt
├── Dockerfile
├── README.md
└── run_backtest.py            # CLI to run the full pipeline
```
