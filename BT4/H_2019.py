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
#print(X)

Y = dt.price
#print(Y)

'''
Hiển thị dữ liệu tương quan giữa diện tích (lotsize) và giá nhà (price)

'''
plt.scatter(dt.lotsize, dt.price)
plt.show()

# Huan luyen mo hinh

nl = linear_model.LinearRegression()
