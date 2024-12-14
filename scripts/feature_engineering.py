import pandas as pd

# Moving Averages
def add_moving_averages(data, short_window=10, long_window=50):
    data[f'SMA_{short_window}'] = data['close'].rolling(window=short_window).mean()
    data[f'SMA_{long_window}'] = data['close'].rolling(window=long_window).mean()
    data[f'EMA_{short_window}'] = data['close'].ewm(span=short_window, adjust=False).mean()
    data[f'EMA_{long_window}'] = data['close'].ewm(span=long_window, adjust=False).mean()
    return data

# MACD (Moving Average Convergence Divergence)
def add_macd(data):
    data['EMA_12'] = data['close'].ewm(span=12, adjust=False).mean()
    data['EMA_26'] = data['close'].ewm(span=26, adjust=False).mean()
    data['MACD'] = data['EMA_12'] - data['EMA_26']
    data['Signal_Line'] = data['MACD'].ewm(span=9, adjust=False).mean()
    return data

# RSI (Relative Strength Index)
def add_rsi(data, period=14):
    delta = data['close'].diff()
    gain = (delta.where(delta > 0, 0)).rolling(window=period).mean()
    loss = (-delta.where(delta < 0, 0)).rolling(window=period).mean()
    rs = gain / loss
    data['RSI'] = 100 - (100 / (1 + rs))
    return data

# ADX (Average Directional Index)
def add_adx(data, period=14):
    data['High_Low'] = data['high'] - data['low']
    data['High_Close'] = abs(data['high'] - data['close'].shift(1))
    data['Low_Close'] = abs(data['low'] - data['close'].shift(1))
    data['TR'] = data[['High_Low', 'High_Close', 'Low_Close']].max(axis=1)

    data['+DM'] = data['high'].diff()
    data['-DM'] = data['low'].diff()
    data['+DM'] = data['+DM'].where((data['+DM'] > 0) & (data['+DM'] > data['-DM']), 0)
    data['-DM'] = data['-DM'].where((data['-DM'] > 0) & (data['-DM'] > data['+DM']), 0)

    data['TR_14'] = data['TR'].rolling(window=period).mean()
    data['+DI_14'] = 100 * (data['+DM'].rolling(window=period).mean() / data['TR_14'])
    data['-DI_14'] = 100 * (data['-DM'].rolling(window=period).mean() / data['TR_14'])
    data['DX'] = 100 * abs(data['+DI_14'] - data['-DI_14']) / (data['+DI_14'] + data['-DI_14'])
    data['ADX'] = data['DX'].rolling(window=period).mean()
    return data

# Apply all features to a dataset
def add_features(file_name):
    data = pd.read_csv(file_name)

    # Rename columns for consistency
    data.columns = ['date', 'open', 'high', 'low', 'close', 'volume']

    # Convert date to datetime
    data['date'] = pd.to_datetime(data['date'])

    # Add indicators
    data = add_moving_averages(data)
    data = add_macd(data)
    data = add_rsi(data)
    data = add_adx(data)

    # Drop NaN rows (from rolling calculations)
    data.dropna(inplace=True)

    # Save enriched dataset
    enriched_file_name = file_name.replace('.csv', '_enriched.csv')
    data.to_csv(enriched_file_name, index=False)
    print(f"Features added and saved to {enriched_file_name}")

# Example usage
if __name__ == "__main__":
    file_names = [
        "data/TSLA_daily_data.csv",
        "data/AMZN_daily_data.csv",
        # Add other stock files here
    ]
    for file in file_names:
        add_features(file)
