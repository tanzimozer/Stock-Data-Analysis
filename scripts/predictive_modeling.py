import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor, RandomForestClassifier
from sklearn.metrics import mean_squared_error, r2_score, accuracy_score, classification_report, ConfusionMatrixDisplay
import matplotlib.pyplot as plt

# Prepare data for regression and classification
def prepare_model_data(file_name):
    data = pd.read_csv(file_name)

    # Define features and targets
    features = ['SMA_10', 'EMA_10', 'MACD', 'RSI', 'ADX']
    X = data[features]

    # Regression target: Next day’s closing price
    data['Target_Regression'] = data['close'].shift(-1)

    # Classification target: Price movement direction (Up/Down)
    data['Target_Classification'] = (data['close'].shift(-1) > data['close']).astype(int)

    # Drop rows with NaN (caused by shifting)
    data.dropna(subset=['Target_Regression', 'Target_Classification'], inplace=True)

    # Ensure X matches the rows of y
    X = X.iloc[:-1]  # Remove the last row to match shifted targets

    # Targets
    y_reg = data['Target_Regression']
    y_class = data['Target_Classification']

    # Split data
    X_train_reg, X_test_reg, y_train_reg, y_test_reg = train_test_split(X, y_reg, test_size=0.2, random_state=42)
    X_train_class, X_test_class, y_train_class, y_test_class = train_test_split(X, y_class, test_size=0.2, random_state=42)

    return X_train_reg, X_test_reg, y_train_reg, y_test_reg, X_train_class, X_test_class, y_train_class, y_test_class

# Train and evaluate regression model
def train_regression_model(X_train, X_test, y_train, y_test):
    rf_reg = RandomForestRegressor(n_estimators=100, random_state=42)
    rf_reg.fit(X_train, y_train)
    y_pred = rf_reg.predict(X_test)

    print("Regression Model Evaluation:")
    print(f"Mean Squared Error: {mean_squared_error(y_test, y_pred):.2f}")
    print(f"R² Score: {r2_score(y_test, y_pred):.2f}")

    # Plot actual vs predicted
    plt.figure(figsize=(10, 6))
    plt.plot(y_test.values, label='Actual Prices', alpha=0.7)
    plt.plot(y_pred, label='Predicted Prices', alpha=0.7)
    plt.title("Regression: Actual vs Predicted Prices")
    plt.xlabel("Test Index")
    plt.ylabel("Stock Price")
    plt.legend()
    plt.show()

# Train and evaluate classification model
def train_classification_model(X_train, X_test, y_train, y_test):
    rf_class = RandomForestClassifier(n_estimators=100, random_state=42)
    rf_class.fit(X_train, y_train)
    y_pred = rf_class.predict(X_test)

    print("Classification Model Evaluation:")
    print(f"Accuracy: {accuracy_score(y_test, y_pred):.2f}")
    print("\nClassification Report:")
    print(classification_report(y_test, y_pred))

    # Confusion Matrix
    ConfusionMatrixDisplay.from_estimator(rf_class, X_test, y_test, cmap="Blues")
    plt.title("Classification Confusion Matrix")
    plt.show()

# Example usage
if __name__ == "__main__":
    file_names = [
        "data/TSLA_daily_data_enriched.csv",
        # Add other stock files here
    ]

    for file in file_names:
        try:
            print(f"Processing file {file}...")
            # Prepare data
            X_train_reg, X_test_reg, y_train_reg, y_test_reg, X_train_class, X_test_class, y_train_class, y_test_class = prepare_model_data(file)

            # Train and evaluate models
            print("\nTraining Regression Model...")
            train_regression_model(X_train_reg, X_test_reg, y_train_reg, y_test_reg)

            print("\nTraining Classification Model...")
            train_classification_model(X_train_class, X_test_class, y_train_class, y_test_class)

        except Exception as e:
            print(f"Error processing file {file}: {e}")
