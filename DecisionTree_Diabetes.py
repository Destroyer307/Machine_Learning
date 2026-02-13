import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score

data = pd.read_csv('diabetes.csv')

df = pd.DataFrame(data)

a = df.head()
print(a)

X = df[['Glucose','BloodPressure','Age','BMI','SkinThickness','Insulin','DiabetesPedigreeFunction','Pregnancies']]
y = df['Outcome']
X_train , X_test , y_train , y_test = train_test_split(X,y , test_size=0.15 , random_state=42)

classifier = DecisionTreeClassifier()
classifier.fit(X_train,y_train)

y_pred = classifier.predict(X_test)

accuracy_score1 = accuracy_score(y_test,y_pred)
print(f"Modelin doğruluk oranı :{accuracy_score1}")