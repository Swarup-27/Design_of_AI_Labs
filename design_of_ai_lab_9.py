# -*- coding: utf-8 -*-
"""Design_of_AI_Lab_9.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1d01tZM3qwSw3LP6VJgzfomYYgPwbeptW
"""

import pandas as pd
import numpy as np
from sklearn.datasets import load_breast_cancer

data=load_breast_cancer()
data

from sklearn.model_selection import train_test_split
X_train,X_test,y_train,y_test=train_test_split(data.data,data.target,random_state=1,test_size=0.2)

from sklearn.preprocessing import StandardScaler
scaler=StandardScaler()
X_train_scaled=scaler.fit_transform(X_train)
X_test_scaled=scaler.fit_transform(X_test)

from sklearn.naive_bayes import GaussianNB
GNB=GaussianNB()
GNB.fit(X_train,y_train)
GNB.score(X_test,y_test)

from sklearn.naive_bayes import MultinomialNB
MNB=MultinomialNB()
MNB.fit(X_train,y_train)
MNB.score(X_test,y_test)

from sklearn.naive_bayes import BernoulliNB
BNB=BernoulliNB()
BNB.fit(X_train,y_train)
BNB.score(X_test,y_test)

#Probability
test=X_test[0]
test=np.array([test])
GNB.predict_proba(test)

GNB.predict(test)