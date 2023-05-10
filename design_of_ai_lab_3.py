# -*- coding: utf-8 -*-
"""Design_of_AI_Lab_3.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/17fseWBzjK8DSY2DSeHITlJASOwif9sKS
"""

import pandas as pd
data=pd.read_csv('/content/diabetes.csv')
data

data=data.values
X=data[:,0:-1]
Y=data[:,-1]

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler

X_train,X_test,y_train,y_test=train_test_split(X,Y,random_state=1,test_size=0.2)

scaler=StandardScaler()
X_train_scaled=scaler.fit_transform(X_train)
X_test_scaled=scaler.fit_transform(X_test)

#1) Logistic Regression
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import roc_auc_score
log_reg=LogisticRegression(max_iter=1000)

model1=log_reg.fit(X_train,y_train)

y_predict1=model1.predict(X_test)

roc_auc_score(y_test,y_predict1)

from sklearn.metrics import confusion_matrix
cm=confusion_matrix(y_test,y_predict1)
cm



#2)SVM
from sklearn.svm import SVC
svm=SVC(kernel='linear')
model2=svm.fit(X_train,y_train)

y_predict2=model2.predict(X_test)

roc_auc_score(y_test,y_predict2)

from sklearn.metrics import confusion_matrix,roc_auc_score
cm=confusion_matrix(y_test,y_predict2)
cm



#3) KNN
from sklearn.neighbors import KNeighborsClassifier
knn=KNeighborsClassifier(n_neighbors=10,metric='minkowski',p=2)
model3=knn.fit(X_train,y_train)

y_predict3=model3.predict(X_test)

roc_auc_score(y_test,y_predict3)

cm=confusion_matrix(y_test,y_predict3)
cm

