# Stock-Data-Analysis
Stock Market Analysis: Predicting Prices and Movements

This project analyzes stock market data for 10 major companies (Tesla, Amazon, Microsoft, Starbucks, Apple, Nvidia, Chase Bank, Robinhood, BlackRock, and Google) using Python. We employ technical indicators and machine learning models to predict stock prices and price direction.

Project Overview
Objective: Use technical analysis and machine learning to predict:
Next day's closing price (Regression).
Whether the price will go up or down (Classification).

Key Features:
Technical Indicators: SMA, EMA, MACD, RSI, ADX.
Models: Random Forest Regressor and Classifier.
Visualization: Actual vs Predicted Prices, Confusion Matrix, and Correlation Heatmaps.

Project Workflow
Data Collection:
Fetched historical stock data from Alpha Vantage.
Saved raw data as .csv files for each company.

Feature Engineering:
Generated technical indicators (e.g., SMA, EMA, MACD, RSI, ADX) for enriched datasets.
Exploratory Data Analysis (EDA):
Visualized stock trends with SMA/EMA.
Analyzed momentum indicators (MACD, RSI).
Explored feature correlations using heatmaps.
Predictive Modeling:
Regression: Predicted next day's closing price.
Classification: Predicted price direction (Up/Down).
Evaluated models using metrics like MSE, R², and Accuracy.
Visualization and Reporting:
Visualized predictions and confusion matrices.
Summarized key metrics and correlations.
Results

Regression:
Example (Tesla): MSE = 10.32, R² = 0.89.
Classification:
Example (Tesla): Accuracy = 85.6%.
See models/ directory for detailed metrics.

Project Files
data/: Enriched datasets for all 10 stocks.
models/: Saved model performance metrics.
scripts/: Python scripts for data processing, analysis, and modeling.

README.md: Project summary and instructions.
requirements.txt: Dependencies for the project.

Usage:
Clone the repository:
git clone https://github.com/t/anzimzoer/stock-data-analysis.git
cd stock-data-analysis
pip install -r requirements.txt

Run the scripts:
Data Collection: python scripts/data_collection.py
Feature Engineering: python scripts/feature_engineering.py
EDA: python scripts/exploratory_data_analysis.py
Modeling: python scripts/predictive_modeling.py

Dependencies
Python (>=3.8)
pandas
numpy
scikit-learn
matplotlib
seaborn
Alpha Vantage API key (free at Alpha Vantage).

________________________________________________________________
stock-market-analysis/
├── data/                # Folder for raw and enriched datasets
├── models/              # Folder for model evaluation metrics
├── scripts/             # Folder for all Python scripts
│   ├── data_collection.py
│   ├── feature_engineering.py
│   ├── exploratory_data_analysis.py
│   ├── predictive_modeling.py
│   └── visualization_and_reporting.py
├── README.md            # The file you just created
├── requirements.txt     # File for dependencies
