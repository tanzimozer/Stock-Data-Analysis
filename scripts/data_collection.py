from alpha_vantage.timeseries import TimeSeries
import pandas as pd

# Replace with your API key
api_key = 'S2777LSDBW510FV3'

# Initialize Alpha Vantage API
ts = TimeSeries(key=api_key, output_format='pandas')

# List of stocks to fetch
stocks = ['TSLA', 'AMZN', 'MSFT', 'SBUX', 'AAPL', 'NVDA', 'JPM', 'HOOD', 'BLK', 'GOOGL']

# Fetch and save data
for stock in stocks:
    print(f"Fetching data for {stock}...")
    data, meta_data = ts.get_daily(symbol=stock, outputsize='full')
    data.to_csv(f"data/{stock}_daily_data.csv")
    print(f"Data saved for {stock}")
