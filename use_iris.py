
from sklearn.datasets import load_iris
iris_dt = load_iris()
iris_dt.data[1:5]
iris_dt.target[1:5]

from sklearn.model_selection import train_test_split

X_train, X_test, Y_train, Y_test = train_test_split(iris_dt.data, iris_dt.target, test_size=1/3.0, random_state=5)

X_train
X_test
Y_train
Y_test

from sklearn.neighbors import KNeighborsClassifier
Mohinh_KNN = KNeighborsClassifier(n_neighbors=7)
Mohinh_KNN.fit(X_train,Y_train)

y_pred = Mohinh_KNN.predict(X_test)
Y_test
Mohinh_KNN.predict([[4, 4, 3, 3]])

from sklearn.metrics import accuracy_score
print("Accuracy is ",accuracy_score(Y_test,y_pred,)*100)