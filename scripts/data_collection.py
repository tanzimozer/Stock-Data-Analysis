from alpha_vantage.timeseries import TimeSeries
import pandas as pd
import os
import time

# Replace with your API key
api_key = 'S2777LSDBW510FV3'

# Initialize Alpha Vantage API
ts = TimeSeries(key=api_key, output_format='pandas')

# Ensure 'data/' directory exists
if not os.path.exists('data'):
    os.makedirs('data')

# List of stocks to fetch
stocks = ['TSLA', 'AMZN', 'MSFT', 'SBUX', 'AAPL', 'NVDA', 'JPM', 'HOOD', 'BLK', 'GOOGL']

# Fetch and save data
for stock in stocks:
    try:
        print(f"Fetching data for {stock}...")
        
        # Fetch data from Alpha Vantage
        data, meta_data = ts.get_daily(symbol=stock, outputsize='full')
        
        # Save data to 'data/' directory
        data.to_csv(f"data/{stock}_daily_data.csv")
        print(f"Data saved for {stock}")
        
        # Respect Alpha Vantage's rate limit
        time.sleep(12)  # Wait 12 seconds before the next call (5 calls per minute allowed)
    
    except Exception as e:
        print(f"Failed to fetch data for {stock}: {e}")
