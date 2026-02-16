# Algerian Forest Fires – Linear Regression

This project builds a machine learning model to predict the *FWI (Fire Weather Index)* using weather and fire-related measurements from the Algerian forest fires dataset.

The workflow includes data cleaning, preprocessing, exploratory data analysis, and training a Linear Regression model.

---

## Dataset

The dataset contains daily weather observations and fire indicators.

Main variables:

- day, month, year  
- Temperature  
- RH (Relative Humidity)  
- Ws (Wind speed)  
- Rain  
- FFMC, DMC, DC, ISI, BUI  
- FWI (target variable)  
- Classes (fire / not fire)  
- Region  

---

## Data Preprocessing

The following steps were applied:

- Removed problematic or unnecessary rows.
- Cleaned column names (trimmed spaces).
- Converted numeric columns to proper data types.
- Transformed *Classes* into binary values:
  - not fire → 0
  - fire → 1

---

## Exploratory Data Analysis

- Checked for missing values.
- Examined data types and distributions.
- Generated a *correlation matrix*.
- Visualized correlations using a heatmap.

---

## Feature & Target Selection

- *X (features):* All variables except FWI.
- *y (target):* FWI.

---

## Feature Scaling

Standardization was applied using StandardScaler to normalize feature ranges before training.

---

## Model

LinearRegression from scikit-learn was used.

Steps:
1. Split data into train and test sets.
2. Fit the model on training data.
3. Predict on test data.

---

## Evaluation

Model performance was measured using:

- *R² Score*
- Mean Absolute Error (MAE)
- Mean Squared Error (MSE)

Example result from the notebook: R2_SCORE = 0.98
