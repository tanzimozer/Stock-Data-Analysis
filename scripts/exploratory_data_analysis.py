import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Plot stock price trends with SMA/EMA
def plot_price_trends(file_name):
    data = pd.read_csv(file_name)
    data['date'] = pd.to_datetime(data['date'])

    plt.figure(figsize=(12, 6))
    plt.plot(data['date'], data['close'], label='Closing Price', alpha=0.7)
    plt.plot(data['date'], data['SMA_10'], label='10-Day SMA', linestyle='--')
    plt.plot(data['date'], data['EMA_10'], label='10-Day EMA', linestyle='--')
    plt.title(f"Stock Price Trends for {file_name.split('/')[-1].split('_')[0]}")
    plt.xlabel('Date')
    plt.ylabel('Price')
    plt.legend()
    plt.show()

# Plot MACD
def plot_macd(file_name):
    data = pd.read_csv(file_name)
    data['date'] = pd.to_datetime(data['date'])

    plt.figure(figsize=(12, 6))
    plt.plot(data['date'], data['MACD'], label='MACD', color='blue')
    plt.plot(data['date'], data['Signal_Line'], label='Signal Line', color='red', linestyle='--')
    plt.title(f"MACD for {file_name.split('/')[-1].split('_')[0]}")
    plt.xlabel('Date')
    plt.ylabel('MACD Value')
    plt.legend()
    plt.show()

# Plot RSI
def plot_rsi(file_name):
    data = pd.read_csv(file_name)
    data['date'] = pd.to_datetime(data['date'])

    plt.figure(figsize=(12, 6))
    plt.plot(data['date'], data['RSI'], label='RSI', color='purple')
    plt.axhline(70, color='red', linestyle='--', label='Overbought (70)')
    plt.axhline(30, color='green', linestyle='--', label='Oversold (30)')
    plt.title(f"RSI for {file_name.split('/')[-1].split('_')[0]}")
    plt.xlabel('Date')
    plt.ylabel('RSI Value')
    plt.legend()
    plt.show()

# Correlation Heatmap
def plot_correlation_heatmap(file_name):
    data = pd.read_csv(file_name)
    corr_matrix = data[['close', 'SMA_10', 'EMA_10', 'MACD', 'RSI', 'ADX']].corr()

    plt.figure(figsize=(8, 6))
    sns.heatmap(corr_matrix, annot=True, cmap='coolwarm', fmt=".2f")
    plt.title(f"Correlation Heatmap for {file_name.split('/')[-1].split('_')[0]}")
    plt.show()

# Example usage
if __name__ == "__main__":
    file_names = [
        "data/TSLA_daily_data_enriched.csv",
        "data/AMZN_daily_data_enriched.csv",
        # Add other stock files here
    ]
    for file in file_names:
        print(f"Analyzing {file}...")
        plot_price_trends(file)
        plot_macd(file)
        plot_rsi(file)
        plot_correlation_heatmap(file)
