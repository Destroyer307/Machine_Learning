# Customer Subscription Prediction

This project builds a binary classification model using Logistic Regression to predict whether a customer subscribes (0 = No, 1 = Yes).

## Features
- age
- job_satisfaction
- balance
- duration_last_call
- num_contacts_last_month
- has_housing_loan

## Method
- Train/Test Split (80/20, random_state=42)
- Logistic Regression
- Evaluation: Accuracy, Classification Report, Confusion Matrix
- Hyperparameter tuning with GridSearchCV and RandomizedSearchCV
- StratifiedKFold cross-validation

## Results
- Test Accuracy: 0.93
- Best GridSearch Params: C=0.1, penalty=l1, solver=liblinear
- Best RandomSearch Params: C=0.1, penalty=l2, solver=saga

Logistic Regression achieved strong performance (~93% accuracy) on this dataset.
