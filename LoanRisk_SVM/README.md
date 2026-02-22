# Loan Risk Classification with SVM

## Overview
This project predicts loan risk using Support Vector Machines (SVM).

Target:
- 0 → Not Risky  
- 1 → Risky  

Features:
- credit_score_fluctuation
- recent_transaction_volume

---

## Dataset
- 1000 samples
- No missing values
- Binary classification problem

---

## Models Used
- Linear SVM
- RBF SVM
- Sigmoid SVM

Best performance achieved with *RBF kernel*.

---

## Hyperparameter Tuning
Used GridSearchCV with:

```python
param_grid = {
    "C": [0.1, 1, 10, 100, 1000],
    "kernel": ["rbf"],
    "gamma": ["scale", "auto"]
}
## Best Params :
{'C': 1000, 'gamma': 'auto', 'kernel': 'rbf'}
Accuracy: 0.93
Precision: 0.93
Recall: 0.93
F1-score: 0.93
