# 📈 Linear vs Polynomial Regression – Customer Satisfaction

This project compares *Linear Regression* and *Polynomial Regression* on the same dataset.  
The goal is to observe how feature expansion with polynomial terms can improve the model’s ability to capture non-linear relationships.

## 🚀 Project Objective
- Apply a baseline linear regression model  
- Increase model capacity with feature engineering  
- Compare performances using the *R² score*  
- Visualize predictions for better interpretation

## 🧠 Methods Used
- Train / Test Split  
- Data scaling with StandardScaler  
- Linear Regression  
- Polynomial Features (degree = 2)  
- R² Score  
- Scatter plot visualization

## 🗂 Dataset
The model is trained on a CSV dataset that represents the relationship between *customer satisfaction* and *incentives*.

## ⚙️ Steps Performed
1. Loaded the dataset using pandas.  
2. Removed unnecessary columns.  
3. Defined independent and dependent variables.  
4. Split data into training and test sets.  
5. Applied standardization.  
6. Trained and evaluated the Linear Regression model.  
7. Generated polynomial features and retrained the model.  
8. Compared performance metrics.  
9. Visualized predictions on a graph.

## 📊 Evaluation
Model performance is measured with *R² (coefficient of determination)*.  
The improvement of the polynomial model over the linear model is analyzed.

## 🛠 Libraries
- pandas  
- numpy  
- matplotlib  
- seaborn  
- scikit-learn  

## ▶️ Run the Project
bash
pip install pandas numpy matplotlib seaborn scikit-learn
python PolynomialRegression_CustomerSatisfaction.py


## 🎯 Key Learnings
Through this project, I practiced:
- Regression modeling  
- Data preprocessing  
- Feature engineering  
- Model evaluation  
- Building a simple ML workflow
