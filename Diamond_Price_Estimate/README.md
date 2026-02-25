# 💎 Diamond Price Prediction with SVR

This project builds a machine learning model to predict diamond prices using the *Diamonds dataset* and *Support Vector Regression (SVR)*.

## 📌 Project Steps

### 1️⃣ Data Preprocessing
- Loaded dataset (diamonds.csv)
- Removed unnecessary column: Unnamed: 0
- Removed invalid records (x, z = 0)
- Applied filtering on table and depth
- Encoded categorical variables:
  - cut
  - color
  - clarity
- Split data into train/test (80/20)
- Applied StandardScaler

### 2️⃣ Model
- Algorithm: SVR
- Hyperparameter tuning using GridSearchCV
- 5-fold Cross Validation
- Parameter Grid:
  - C: [1, 10, 100]
  - gamma: [1, 0.1, 0.01]
  - kernel: ['rbf', 'linear']

### 3️⃣ Best Parameters
python
{'C': 100, 'gamma': 0.1, 'kernel': 'rbf'}


### 4️⃣ Model Performance
- *R² Score:* 0.9313

## 📊 Result
The SVR model achieved strong performance with ~93% variance explanation on test data.

---

### 🛠 Technologies Used
- Python
- Pandas
- NumPy
- Seaborn
- Scikit-learn
- Matplotlib
