#su dung thu vien pandas
import pandas as pd
dt = pd.read_csv("winequality-white.csv",delimiter=';')
#in dữ liệu ra màn hình
print("=================== a. IN DU LIEU ================")
print (dt)
#su dung thu vien numpy
import numpy as np
print("=================== b. dem du lieu ================")
print(dt.quality.value_counts())
#su dung KFold
from sklearn.model_selection import KFold
X=dt.iloc[:,0:11]
y=dt.iloc[:,11]
kf=KFold(n_splits=50,shuffle=True)
for train_index, test_index in kf.split(X):
   # print("Train:",train_index,"Test:", test_index)
    X_train, X_test = X.iloc[train_index,], X.iloc[test_index,]
    y_train, y_test = y.iloc[train_index], y.iloc[test_index]
    #print ("X_test",X_test)    
    from sklearn.tree import DecisionTreeClassifier
    clf_gini=DecisionTreeClassifier(criterion="gini", random_state=100, max_depth=3, min_samples_leaf=5)
    clf_gini.fit(X_train, y_train) 
    y_pred=clf_gini.predict(X_test)
    y_test
    from sklearn.metrics import accuracy_score
    print("Accuracy is", accuracy_score(y_test,y_pred)*100)
#KNN
from sklearn.model_selection import train_test_split
X_train_2, X_test_2, y_train_2, y_test_2 = train_test_split(dt.iloc[:,0:11],dt.iloc[:,11],test_size=1/3.0,random_state=5)
from sklearn.neighbors import KNeighborsClassifier
Mohinh_KNN=KNeighborsClassifier(n_neighbors=5)
Mohinh_KNN.fit(X_train_2,y_train_2)
y_pred_2=Mohinh_KNN.predict(X_test_2)
y_test_2
from sklearn.metrics import accuracy_score
print("KNN: Accuracy is", accuracy_score(y_test_2,y_pred_2)*100)

from sklearn.naive_bayes import GaussianNB
from sklearn.naive_bayes import MultinomialNB
from sklearn.model_selection import train_test_split
X_train_3, X_test_3, y_train_3, y_test_3 = train_test_split(dt.iloc[:,0:11],dt.iloc[:,11],test_size=0.3,random_state=0)
MohinhBY=GaussianNB()
MohinhBY.fit(X_train_3,y_train_3)
thucte=y_test_3
dubao=MohinhBY.predict(X_test_3)
print("Bayes: Accuracy is", accuracy_score(thucte,dubao)*100)

