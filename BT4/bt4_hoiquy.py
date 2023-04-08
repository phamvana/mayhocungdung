import pandas as pd
from sklearn.metrics import mean_squared_error
import numpy as np

dt=pd.read_csv("Housing_2019.csv", index_col=0)
X=dt.iloc[:,[1,2,4,10]]
Y=dt.price

# print("Gia tri cua X \n",X)
# print("Gia tri cua Y \n",Y)
#print(X, " ",Y)

import sklearn
from sklearn.model_selection import train_test_split

X_train, X_test, y_train, y_test = train_test_split(X,Y,test_size=1.0/3, random_state=100)

print(len(X_train))

from sklearn.ensemble import BaggingRegressor
from sklearn import linear_model
lm=linear_model.LinearRegression()
bagging_reg= BaggingRegressor(estimator=lm,n_estimators=10,random_state=42)
bagging_reg.fit(X_train,y_train)

y_pred = bagging_reg.predict(X_test)
err=mean_squared_error(y_test,y_pred)

print("Err: ",err)
print("SQRT Err: ", np.sqrt(err))