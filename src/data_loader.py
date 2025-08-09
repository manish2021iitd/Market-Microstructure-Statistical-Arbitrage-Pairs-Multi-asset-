import pandas as pd
import yfinance as yf
from datetime import datetime

def fetch_data(tickers, start, end, interval='1d'):
    data = {}
    for ticker in tickers:
        df = yf.download(ticker, start=start, end=end, interval=interval)
        df = df[['Adj Close']].rename(columns={'Adj Close': ticker})
        data[ticker] = df
    prices = pd.concat(data.values(), axis=1)
    prices.columns = tickers
    return prices.dropna()

if __name__ == "__main__":
    tickers = ['MSFT', 'AAPL', 'GOOG']
    df = fetch_data(tickers, "2020-01-01", "2023-01-01")
    df.to_csv("../data/prices.csv")

