# Gold Price Prediction using Random Forest Regression

A machine learning-based application that predicts gold prices using financial market indicators and the Random Forest Regression algorithm. The project integrates supervised machine learning with an interactive Streamlit web application to generate gold price predictions from user-provided market data.

## Overview

This project implements a supervised machine learning regression model to estimate gold prices based on selected financial market indicators.

It uses the **Random Forest Regressor**, an ensemble learning algorithm that combines multiple decision trees to generate numerical predictions.

The model takes four input features:

- **SPX:** S&P 500 stock market index.
- **SLV:** Silver price indicator.
- **EUR/USD:** Euro-to-US-dollar exchange rate.
- **USO:** United States Oil Fund price indicator.

A trained Random Forest model processes these inputs and predicts the corresponding gold price.

The application is deployed using **Streamlit**, providing an interactive interface through which users can enter financial indicators and obtain predictions.

## Key Features

- **Gold Price Prediction:** Estimates gold prices using financial market indicators.
- **Supervised Machine Learning:** Implements a regression-based predictive modeling approach.
- **Random Forest Regression:** Uses an ensemble of decision trees for numerical prediction.
- **Multiple Financial Indicators:** Incorporates SPX, SLV, EUR/USD, and USO as model input features.
- **Pre-trained Model Integration:** Loads a previously trained model using Python Pickle.
- **Interactive Web Application:** Provides a Streamlit interface for user input and real-time predictions.
- **Numerical Prediction:** Generates continuous-valued gold price estimates.

## Machine Learning Workflow

The system follows a straightforward machine learning prediction pipeline:

1. **User Input:** Collects four financial indicators through the Streamlit interface.
2. **Input Processing:** Splits the comma-separated values and converts them into numerical data.
3. **Feature Preparation:** Arranges the input values into a two-dimensional NumPy array.
4. **Model Loading:** Loads the pre-trained Random Forest Regressor from the serialized model file.
5. **Price Prediction:** Passes the processed features to the model to generate a gold price estimate.
6. **Result Display:** Presents the predicted gold price through the Streamlit interface.

## Technology Stack

| Category | Technologies |
|---|---|
| Programming Language | Python |
| Machine Learning | Scikit-learn |
| Regression Algorithm | Random Forest Regressor |
| Data Processing | NumPy |
| Web Application | Streamlit |
| Model Serialization | Pickle |
| Development Environment | Python IDE |




## Usage

The application requires four comma-separated numerical inputs in the following order:

```text
SPX, SLV, EUR/USD, USO
```

**Example Input**

```text
4500, 22.5, 1.08, 75
```

Click the **Predict the gold price** button to generate the prediction.

The trained Random Forest Regressor processes the provided values and displays the estimated gold price.

*Note: The example values are illustrative and are not intended to represent current market prices.*

## Model Implementation

The project uses the **Random Forest Regressor** algorithm from Scikit-learn.

Random Forest is an ensemble learning technique that constructs multiple decision trees and combines their predictions to produce a final numerical output.

The trained model is serialized and stored in:

`ForestRegressor.pkl`

During application execution, the model is loaded using Python's Pickle module and used to perform predictions without requiring retraining.

## Live Demo

Try the deployed application:

[**Gold Price Prediction – Streamlit App**](https://hriiume4wwvyppdvjs6evc.streamlit.app/)

