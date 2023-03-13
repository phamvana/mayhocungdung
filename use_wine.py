from sklearn.datasets import load_wine
wine_dt = load_wine()
wine_dt.data[2:5]
print(wine_dt.data[2:5])
wine_dt.target[2:5]
print(wine_dt.target[2:5])
from sklearn.model_selection import train_test_split

X_train, X_test, Y_train, Y_test = train_test_split(wine_dt.data, wine_dt.target, test_size=2/5.0, random_state=5)

X_train
X_test
Y_train
Y_test

from sklearn.neighbors import KNeighborsClassifier
Mohinh_KNN = KNeighborsClassifier(n_neighbors=7)
Mohinh_KNN.fit(X_train,Y_train)

y_pred = Mohinh_KNN.predict(X_test)
Y_test

Mohinh_KNN.predict([[1, 2, 3, 1, 5, 3, 3, 1, 2, 3, 1, 3, 1]])
from sklearn.metrics import accuracy_score
print("Accuracy is ",accuracy_score(Y_test,y_pred,)*100)