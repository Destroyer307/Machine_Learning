import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.metrics import r2_score , mean_squared_error
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler

df = pd.read_csv("3-customersatisfaction (1).csv")
df.drop("Unnamed: 0" , axis= 1 , inplace=True)

X = df[["Customer Satisfaction"]]
y = df["Incentive"]

X_train , X_test , y_train , y_test = train_test_split(X,y,test_size=0.25,random_state=42)
scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)
model = LinearRegression()
model.fit(X_train,y_train)
y_pred = model.predict(X_test)
score = r2_score(y_test,y_pred)
print(f"Modelin doğruluk oranı :{score}")


poly = PolynomialFeatures(degree=2,include_bias=True)
X_train_poly = poly.fit_transform(X_train)
X_test_poly = poly.transform(X_test)
model.fit(X_train_poly,y_train)
y_pred = model.predict(X_test_poly)
scorex = r2_score(y_test,y_pred)
print(f"Modelin polinomal regresyon uygulanmış halindeki doğruluk oranı :{scorex}")
# Son olarak modelin grafik üzerinde nasıl bir grafik çizdiğini gösterelim
plt.scatter(X_train,y_train)
plt.scatter(X_train , model.predict(X_train_poly) , color ="r")
plt.show()

