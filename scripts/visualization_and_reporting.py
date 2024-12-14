import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.metrics import ConfusionMatrixDisplay

# Plot Regression Results: Actual vs Predicted
def plot_regression_results(y_test, y_pred, title="Regression: Actual vs Predicted"):
    plt.figure(figsize=(10, 6))
    plt.plot(y_test.values, label='Actual Prices', alpha=0.7)
    plt.plot(y_pred, label='Predicted Prices', alpha=0.7)
    plt.title(title)
    plt.xlabel("Test Index")
    plt.ylabel("Stock Price")
    plt.legend()
    plt.show()

# Plot Confusion Matrix for Classification Results
def plot_confusion_matrix(model, X_test, y_test, title="Confusion Matrix"):
    ConfusionMatrixDisplay.from_estimator(model, X_test, y_test)
    plt.title(title)
    plt.show()

# Plot Correlation Heatmap
def plot_correlation_heatmap(file_name):
    data = pd.read_csv(file_name)
    corr_matrix = data[['close', 'SMA_10', 'EMA_10', 'MACD', 'RSI', 'ADX']].corr()

    plt.figure(figsize=(8, 6))
    sns.heatmap(corr_matrix, annot=True, cmap='coolwarm', fmt=".2f")
    plt.title(f"Correlation Heatmap for {file_name.split('/')[-1].split('_')[0]}")
    plt.show()

# Save Performance Metrics
def save_metrics(file_name, regression_mse, regression_r2, classification_accuracy):
    metrics = {
        'Model': ['Regression', 'Classification'],
        'Metric': ['MSE / R²', 'Accuracy'],
        'Value': [f"{regression_mse:.2f} / {regression_r2:.2f}", f"{classification_accuracy:.2f}"]
    }
    metrics_df = pd.DataFrame(metrics)
    metrics_df.to_csv(file_name, index=False)
    print(f"Metrics saved to {file_name}")

# Example usage
if __name__ == "__main__":
    # Example data for plotting (replace with real model outputs)
    y_test_reg = pd.Series([100, 102, 105, 110, 108])  # Example actual prices
    y_pred_reg = [101, 103, 104, 109, 107]  # Example predicted prices

    print("Visualizing Regression Results...")
    plot_regression_results(y_test_reg, y_pred_reg)

    # Confusion matrix example (replace with actual model and test data)
    print("Visualizing Classification Confusion Matrix...")
    # Uncomment the next two lines and provide actual classifier model and test data
    # plot_confusion_matrix(your_classifier_model, X_test_class, y_test_class)

    # Correlation heatmap
    print("Plotting Correlation Heatmap...")
    plot_correlation_heatmap("data/TSLA_daily_data_enriched.csv")

    # Save metrics example (replace with real metrics)
    save_metrics("models/Tesla_model_metrics.csv", regression_mse=10.32, regression_r2=0.89, classification_accuracy=85.6)
