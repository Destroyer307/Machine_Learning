# Gender Prediction using Height & Weight

## 📌 Project Overview

This project aims to predict a person's *Gender* using their *Height* and *Weight*.

The problem is formulated as a *Binary Classification* task and solved using *Logistic Regression*.

---

## 📊 Dataset Information

The dataset contains the following columns:

| Column  | Description              |
|----------|--------------------------|
| Gender   | Male / Female (Target)   |
| Height   | Height (inches)          |
| Weight   | Weight (pounds)          |

### Dataset Characteristics

- Total samples: 10,000
- Target variable: Gender
- Features used: Height, Weight
- Balanced dataset (Male/Female approximately equal)

---

## ⚙️ Data Preprocessing

1. Converted Gender to numerical values:
   - Male → 1
   - Female → 0

2. Split data into:
   - 80% Training set
   - 20% Test set

3. Applied feature scaling using StandardScaler.

---

## 🧠 Model

The model used:

```python
LogisticRegression()
