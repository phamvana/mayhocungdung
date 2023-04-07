#đọc dữ liệu từ csv
import pandas as  pd
import matplotlib.pyplot as plt
import numpy as np

from sklearn import linear_model
dt = pd.read_csv("Housing_2019.csv", index_col=0)
dt.iloc[2:4,]
#print(dt.head(5))

#Giá trị X
X=dt.iloc[:,[1,2,3,4,10]]
X.iloc[1:5,]
print(X)

Y = dt.price
print(Y)

'''
Hiển thị dữ liệu tương quan giữa diện tích (lotsize) và giá nhà (price)

'''
plt.scatter(dt.lotsize, dt.price)
plt.show()

# Huan luyen mo hinh

lm = linear_model.LinearRegression()
lm.fit(X[1:520],Y[1:520])

print(round(lm.intercept_,3))
print(lm.coef_)

# du bao gi nha cho 20 phan tu cuoi cung trong tap du lieu
y = dt.price
y_test =Y[-20:]
x_test=X[-20:]
y_pred = lm.predict(x_test)
#so sanh gia tri du bao va gia tri thuc te
print("Y_pred",y_pred)
print("y_test: ",y_test)

# danh gia
from sklearn.metrics import mean_squared_error
err = mean_squared_error(y_test,y_pred)
print(round(err,3))
np.sqrt(err)

print("SQRT ERR",np.sqrt(err))
