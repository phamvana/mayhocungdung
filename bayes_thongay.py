from sklearn.naive_bayes import GaussianNB
from sklearn.naive_bayes import MultinomialNB

# read file iris

import pandas as pd
dulieu = pd.read_csv("iris_data.csv", delimiter =',')
print(dulieu)
x = dulieu.iloc[:,0:4]
y = dulieu.nhan

print(x)
print(y)

from sklearn.model_selection import train_test_split
x_train, x_test, y_train, y_test = train_test_split(x,y,test_size=0.3, random_state=5)
mohinh = GaussianNB()
mohinh.fit(x_train,y_train)

print(mohinh)

thucte = y_test
dubao = mohinh.predict(x_test)

print("--------------------------")
print("In thuc te:")
print(thucte)
print("--------------------------")
print("In dao tao:")
print(dubao)

from sklearn.metrics import confusion_matrix
cnf_matrix_gnb = confusion_matrix(thucte, dubao)

print(cnf_matrix_gnb)