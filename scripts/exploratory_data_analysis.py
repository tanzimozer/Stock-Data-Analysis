import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

# Plot stock price trends with SMA/EMA
def plot_price_trends(data, stock_name):
    plt.figure(figsize=(12, 6))
    plt.plot(data['date'], data['close'], label='Closing Price', alpha=0.7)
    plt.plot(data['date'], data['SMA_10'], label='10-Day SMA', linestyle='--')
    plt.plot(data['date'], data['EMA_10'], label='10-Day EMA', linestyle='--')
    plt.title(f"Stock Price Trends for {stock_name}")
    plt.xlabel('Date')
    plt.ylabel('Price')
    plt.legend()
    plt.show()

# Plot MACD
def plot_macd(data, stock_name):
    plt.figure(figsize=(12, 6))
    plt.plot(data['date'], data['MACD'], label='MACD', color='blue')
    plt.plot(data['date'], data['Signal_Line'], label='Signal Line', color='red', linestyle='--')
    plt.title(f"MACD for {stock_name}")
    plt.xlabel('Date')
    plt.ylabel('MACD Value')
    plt.legend()
    plt.show()

# Plot RSI
def plot_rsi(data, stock_name):
    plt.figure(figsize=(12, 6))
    plt.plot(data['date'], data['RSI'], label='RSI', color='purple')
    plt.axhline(70, color='red', linestyle='--', label='Overbought (70)')
    plt.axhline(30, color='green', linestyle='--', label='Oversold (30)')
    plt.title(f"RSI for {stock_name}")
    plt.xlabel('Date')
    plt.ylabel('RSI Value')
    plt.legend()
    plt.show()

# Correlation Heatmap
def plot_correlation_heatmap(data, stock_name):
    corr_matrix = data[['close', 'SMA_10', 'EMA_10', 'MACD', 'RSI', 'ADX']].corr()
    plt.figure(figsize=(8, 6))
    sns.heatmap(corr_matrix, annot=True, cmap='coolwarm', fmt=".2f")
    plt.title(f"Correlation Heatmap for {stock_name}")
    plt.show()

# Main Function
def analyze_stock(file_name):
    try:
        # Load data
        data = pd.read_csv(file_name)
        
        # Ensure 'date' column is parsed correctly
        if 'date' not in data.columns:
            raise ValueError(f"'date' column not found in {file_name}")
        data['date'] = pd.to_datetime(data['date'])
        
        # Extract stock name from file name
        stock_name = os.path.basename(file_name).split('_')[0]
        
        # Plot all metrics
        print(f"Analyzing {stock_name}...")
        plot_price_trends(data, stock_name)
        plot_macd(data, stock_name)
        plot_rsi(data, stock_name)
        plot_correlation_heatmap(data, stock_name)
    except FileNotFoundError:
        print(f"File not found: {file_name}")
    except Exception as e:
        print(f"An error occurred while analyzing {file_name}: {e}")

if __name__ == "__main__":
    # Automatically load all enriched files from 'data/' directory
    data_dir = "data"
    file_names = [os.path.join(data_dir, file) for file in os.listdir(data_dir) if file.endswith('_daily_data_enriched.csv')]
    
    for file in file_names:
        analyze_stock(file)
