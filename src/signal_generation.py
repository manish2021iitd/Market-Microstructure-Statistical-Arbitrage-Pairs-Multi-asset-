import pandas as pd
import numpy as np
import statsmodels.api as sm

def generate_zscore_signal(y, x, entry_threshold=2, exit_threshold=0):
    X = sm.add_constant(x)
    model = sm.OLS(y, X).fit()
    hedge_ratio = model.params[1]
    spread = y - hedge_ratio * x
    zscore = (spread - spread.mean()) / spread.std()
    
    signals = pd.DataFrame(index=y.index)
    signals['zscore'] = zscore
    signals['long'] = zscore < -entry_threshold
    signals['short'] = zscore > entry_threshold
    signals['exit'] = abs(zscore) < exit_threshold
    
    return signals, hedge_ratio

if __name__ == "__main__":
    prices = pd.read_csv("../data/prices.csv", index_col=0, parse_dates=True)
    y, x = prices['MSFT'], prices['AAPL']
    signals, hr = generate_zscore_signal(y, x)
    print("Hedge Ratio:", hr)
    print(signals.head())

