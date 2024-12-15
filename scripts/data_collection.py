import yfinance as yf
import os

# List of stock tickers
tickers = ["TSLA", "AMZN", "MSFT", "SBUX", "AAPL", "NVDA", "JPM", "HOOD", "BLK", "GOOGL"]

# Create directory to save data
output_dir = "data"
os.makedirs(output_dir, exist_ok=True)

# Columns required for processing
required_columns = {"Open", "High", "Low", "Close", "Volume"}

# Fetch and save historical data
for ticker in tickers:
    try:
        stock = yf.Ticker(ticker)
        data = stock.history(period="max")

        # Ensure required columns are present
        if not required_columns.issubset(data.columns):
            print(f"Data for {ticker} is missing required columns. Skipping.")
            continue
        
        # Save data to CSV
        output_file = os.path.join(output_dir, f"{ticker}_daily_data.csv")
        data.reset_index(inplace=True)  # Ensure 'Date' is a column
        data.to_csv(output_file, index=False)
        print(f"Data saved for {ticker} in {output_file}")
    except Exception as e:
        print(f"Error fetching data for {ticker}: {e}")
