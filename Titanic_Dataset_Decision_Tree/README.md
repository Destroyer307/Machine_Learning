Titanic Survival Prediction (Decision Tree)

Overview

This project predicts whether a passenger survived the Titanic disaster using a Decision Tree machine learning model. The goal is to practice basic machine learning steps such as data preprocessing, feature encoding, model training, and hyperparameter tuning.

Dataset

Titanic Dataset with features such as:

- Pclass
- Sex
- Age
- SibSp
- Parch
- Fare
- Embarked

Unnecessary columns like Name, PassengerId and Cabin were removed.

Data Preprocessing

- Checked missing values
- Filled missing Age values with the median
- Encoded Sex and Embarked using LabelEncoder
- Removed remaining missing values

Model

A Decision Tree Classifier was trained and optimized using GridSearchCV.

Result

Model accuracy on the test set:

Accuracy: 82%

Libraries

pandas, numpy, seaborn, matplotlib, scikit-learn

Purpose

This project was created as a beginner machine learning exercise to understand the ML workflow and decision tree models.
