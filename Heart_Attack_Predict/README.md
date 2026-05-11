# ❤️ Heart Attack Prediction with Logistic Regression

This project is a beginner-friendly machine learning project focused on predicting heart attack risk using medical data.

The main purpose of this project was to practice the complete machine learning workflow step by step, including:

- reading datasets with pandas
- handling missing values
- cleaning corrupted data
- converting data types
- visualizing data
- splitting train and test sets
- training a Logistic Regression model
- evaluating model performance

---

# 📁 Dataset

Dataset used:

🔗 https://www.kaggle.com/datasets/imnikhilanand/heart-attack-prediction

The dataset contains several medical features such as:

- age
- sex
- chest pain type (`cp`)
- resting blood pressure (`trestbps`)
- cholesterol (`chol`)
- fasting blood sugar (`fbs`)
- resting ECG (`restecg`)
- maximum heart rate achieved (`thalach`)
- exercise induced angina (`exang`)
- oldpeak
- target column: `num`

The target column (`num`) represents whether heart disease exists or not.

---

# 🧹 Data Cleaning Process

## 1) Reading the Dataset

```python
df = pd.read_csv("data.csv")

```accuracy = 0.821
