import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import r2_score
df = pd.read_csv("2-multiplegradesdataset (1).csv")
X = df[['Study Hours','Sleep Hours','Attendance Rate','Social Media Hours']]
y = df['Exam Score']

X_train , X_test , y_train , y_test = train_test_split(X,y , test_size= 0.25 , random_state=42)
scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)
model = LinearRegression()
model.fit(X_train,y_train)
y_pred = model.predict(X_test)
r2 = r2_score(y_test,y_pred)
print(f"Modelin doğruluk oranı : {r2}")
new_student = [[7,7,70,3]]
a = model.predict(scaler.transform(new_student))
print(f"Öğrencinin tahmini notu : {a}")
