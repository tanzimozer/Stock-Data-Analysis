import yfinance as yf
import os

# Create a list of stock tickers
tickers = [
    "TSLA",    # Tesla
    "AMZN",    # Amazon
    "MSFT",    # Microsoft
    "SBUX",    # Starbucks
    "AAPL",    # Apple
    "NVDA",    # Nvidia
    "JPM",     # Chase Bank (JPMorgan)
    "HOOD",    # Robinhood
    "BLK",     # BlackRock
    "GOOGL"    # Google (Alphabet)
]

# Create a directory to save the data
output_dir = "data"
os.makedirs(output_dir, exist_ok=True)

# Fetch and save historical data for each stock
for ticker in tickers:
    try:
        stock = yf.Ticker(ticker)
        data = stock.history(period="max")
        output_file = os.path.join(output_dir, f"{ticker}_daily_data.csv")
        data.to_csv(output_file)
        print(f"Data saved for {ticker}")
    except Exception as e:
        print(f"Error fetching data for {ticker}: {e}")
