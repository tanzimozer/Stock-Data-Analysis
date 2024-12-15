import yfinance as yf

# Fetch historical data for Tesla
stock = yf.Ticker("TSLA")
data = stock.history(period="max")
data.to_csv("data/TSLA_daily_data.csv")
print("Data saved for TSLA")
