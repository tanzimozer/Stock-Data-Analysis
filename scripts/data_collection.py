from alpha_vantage.timeseries import TimeSeries
import pandas as pd
import os

# Replace with your new API key
api_key = '259BRTASIYO3WICX'

# Initialize Alpha Vantage API
ts = TimeSeries(key=api_key, output_format='pandas')

# List of stocks to fetch
stocks = ['TSLA', 'AMZN', 'MSFT', 'SBUX', 'AAPL', 'NVDA', 'JPM', 'HOOD', 'BLK', 'GOOGL']

# Ensure the data directory exists
os.makedirs("data", exist_ok=True)

# Fetch and save data
for stock in stocks:
    try:
        print(f"Fetching data for {stock}...")
        data, meta_data = ts.get_daily(symbol=stock, outputsize='full')
        
        # Rename columns to ensure compatibility
        data.reset_index(inplace=True)
        data.columns = ['date', 'open', 'high', 'low', 'close', 'volume']
        
        # Save to CSV
        data.to_csv(f"data/{stock}_daily_data.csv", index=False)
        print(f"Data saved for {stock}")
    except Exception as e:
        print(f"An error occurred while fetching data for {stock}: {e}")
