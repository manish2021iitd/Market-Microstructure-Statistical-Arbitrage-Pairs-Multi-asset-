import statsmodels.api as sm
from statsmodels.tsa.stattools import coint
import itertools

def find_cointegrated_pairs(prices, significance=0.05):
    pairs = []
    keys = prices.columns
    for (sym1, sym2) in itertools.combinations(keys, 2):
        score, pvalue, _ = coint(prices[sym1], prices[sym2])
        if pvalue < significance:
            pairs.append((sym1, sym2, pvalue))
    return sorted(pairs, key=lambda x: x[2])

if __name__ == "__main__":
    import pandas as pd
    prices = pd.read_csv("../data/prices.csv", index_col=0, parse_dates=True)
    pairs = find_cointegrated_pairs(prices)
    print("Cointegrated Pairs:", pairs)
