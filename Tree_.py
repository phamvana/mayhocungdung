#Lay file iris truc tiep tu sklearn
from sklearn.datasets import load_iris
iris=load_iris()
print(iris.data[1:5])       #thuoc tinh cua tap iris
print(iris.target[1:5])     #Gia tri cua nham /class

#Phân chia dữ liệu để xây dựng mô hình và kiểm tra theo nghi thức Hold-out
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test= train_test_split(iris.data,iris.target, test_size=1/3.0, random_state=5)
X_train[1:6]
X_train[1:6,1:3]
y_train[1:6]
X_test[6:10]
y_test[6:10]

from sklearn.tree import DecisionTreeClassifier
gini_ct=DecisionTreeClassifier(criterion="gini",random_state=100,max_depth=3, min_samples_leaf=5)
gini_ct.fit(X_train,y_train)
dudoan=gini_ct.predict(X_test)
from sklearn.metrics import accuracy_score
print("Accuracy is", accuracy_score(y_test,dudoan)*100)
from sklearn.metrics import confusion_matrix
print(confusion_matrix(y_test,dudoan, labels=[2,0,1]))