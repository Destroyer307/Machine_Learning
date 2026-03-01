# Heart Disease Prediction (KNN)

## Overview
This project predicts heart disease using the K-Nearest Neighbors (KNN) algorithm with a Kaggle heart dataset.

## Dataset
- 1025 samples  
- 14 features  
- Target: 1 (Disease), 0 (No Disease)

## Steps
- Load dataset with pandas  
- Basic EDA (head, shape, value_counts, pairplot)  
- Train-test split (80% / 20%)  
- Feature scaling with StandardScaler  
- Train KNN (n_neighbors=3)  
- Evaluate with accuracy_score  

## Result
Accuracy: *~93.6%*

## Requirements
numpy  
pandas  
seaborn  
matplotlib  
scikit-learn
