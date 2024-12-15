import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor, RandomForestClassifier
from sklearn.metrics import mean_squared_error, r2_score, accuracy_score, classification_report, ConfusionMatrixDisplay
import matplotlib.pyplot as plt

# Prepare data for regression and classification
def prepare_model_data(file_name):
    try:
        data = pd.read_csv(file_name)

        # Check for required columns
        required_features = ['SMA_10', 'EMA_10', 'MACD', 'RSI', 'ADX', 'close']
        if not set(required_features).issubset(data.columns):
            raise ValueError(f"Missing required features in {file_name}: {set(required_features) - set(data.columns)}")

        # Define features and targets
        features = ['SMA_10', 'EMA_10', 'MACD', 'RSI', 'ADX']
        X = data[features]

        # Regression target: Next day’s closing price
        data['Target_Regression'] = data['close'].shift(-1)
        y_reg = data['Target_Regression']

        # Classification target: Price movement direction (Up/Down)
        data['Target_Classification'] = (data['close'].shift(-1) > data['close']).astype(int)
        y_class = data['Target_Classification']

        # Drop NaN rows caused by shifting
        data.dropna(inplace=True)
        X = X.iloc[:-1]  # Exclude last row to match shifted target

        # Split data
        X_train_reg, X_test_reg, y_train_reg, y_test_reg = train_test_split(X, y_reg, test_size=0.2, random_state=42)
        X_train_class, X_test_class, y_train_class, y_test_class = train_test_split(X, y_class, test_size=0.2, random_state=42)

        return X_train_reg, X_test_reg, y_train_reg, y_test_reg, X_train_class, X_test_class, y_train_class, y_test_class

    except FileNotFoundError:
        print(f"File not found: {file_name}")
        return None, None, None, None, None, None, None, None
    except Exception as e:
        print(f"Error processing file {file_name}: {e}")
        return None, None, None, None, None, None, None, None

# Train and evaluate regression model
def train_regression_model(X_train, X_test, y_train, y_test):
    if X_train is None:
        print("Skipping regression due to data issues.")
        return

    rf_reg = RandomForestRegressor(n_estimators=100, random_state=42)
    rf_reg.fit(X_train, y_train)
    y_pred = rf_reg.predict(X_test)

    print("Regression Model Evaluation:")
    print(f"Mean Squared Error: {mean_squared_error(y_test, y_pred):.2f}")
    print(f"R² Score: {r2_score(y_test, y_pred):.2f}")

    # Plot actual vs predicted
    plt.figure(figsize=(10, 6))
    plt.plot(range(len(y_test)), y_test.values, label='Actual Prices', alpha=0.7)
    plt.plot(range(len(y_pred)), y_pred, label='Predicted Prices', alpha=0.7)
    plt.title("Regression: Actual vs Predicted Prices")
    plt.xlabel("Test Index")
    plt.ylabel("Stock Price")
    plt.legend()
    plt.show()

# Train and evaluate classification model
def train_classification_model(X_train, X_test, y_train, y_test):
    if X_train is None:
        print("Skipping classification due to data issues.")
        return

    rf_class = RandomForestClassifier(n_estimators=100, random_state=42)
    rf_class.fit(X_train, y_train)
    y_pred = rf_class.predict(X_test)

    print("Classification Model Evaluation:")
    print(f"Accuracy: {accuracy_score(y_test, y_pred):.2f}")
    print("Classification Report:")
    print(classification_report(y_test, y_pred))

    # Confusion Matrix
    ConfusionMatrixDisplay.from_estimator(rf_class, X_test, y_test, cmap="Blues")
    plt.title("Confusion Matrix")
    plt.show()

if __name__ == "__main__":
    # Example file path
    file_name = "data/TSLA_daily_data_enriched.csv"

    # Prepare data
    (
        X_train_reg, X_test_reg, y_train_reg, y_test_reg,
        X_train_class, X_test_class, y_train_class, y_test_class
    ) = prepare_model_data(file_name)

    # Train and evaluate models
    print("\nTraining Regression Model...")
    train_regression_model(X_train_reg, X_test_reg, y_train_reg, y_test_reg)

    print("\nTraining Classification Model...")
    train_classification_model(X_train_class, X_test_class, y_train_class, y_test_class)
