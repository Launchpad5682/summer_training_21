from sklearn.metrics import mean_squared_error as mse
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from numpy import asarray
import numpy as np

data = pd.read_csv("./dataset/salary.csv")

X = asarray(data['YearsExperience'])
y = asarray(data['Salary'])

X = X.reshape(-1, 1)

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42)

model = LinearRegression()
model.fit(X_train, y_train)

print("Model coefficients: {}".format(model.coef_))
print("Model bias: {}".format(model.intercept_))

result = model.predict(X_test)

print("MSE: {}" .format(mse(y_test, result)))
