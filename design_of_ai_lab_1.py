# -*- coding: utf-8 -*-
"""Design_of_AI_Lab-1.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1xsLOwn1pM5j9m06oC4qSpIyP2IEWLQuI
"""

import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split

# Load the Iris dataset (assuming it's available in scikit-learn)
from sklearn.datasets import load_iris
iris = load_iris()

# Create a DataFrame from the dataset
df = pd.DataFrame(data=iris.data, columns=iris.feature_names)
df['target'] = iris.target

# 1. Check the variable types
print(df.dtypes)

#2. Separate the dependent and independent variables
X = df.drop('target', axis=1)  # Independent variables
Y = df['target']  # Dependent variable
print(Y)

# 3. Handle missing data (NaN values)
# Check if there are any missing values
print(df.isnull().sum())

# As the Iris dataset is a well-known dataset, it usually doesn't contain missing values.
# If there were any missing values, you could handle them using imputation or other methods.

# 4. Encode categorical data (not applicable for the Iris dataset)

# 5. Split the data into training and test sets
X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.2, random_state=42)

# 6. Apply feature scaling (Standardization) to the data
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

# The importance of feature scaling is to ensure that all features have similar scales.
# This can help improve the performance of certain machine learning algorithms that are sensitive to the scale of features.









import pandas as pd
import numpy as np
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler

iris=load_iris()
df=pd.DataFrame(data=iris.data,columns=iris.feature_names)
df['target']=iris.target
df

#1) dtypes
df.dtypes

#2) null values
df.isnull().sum()

#3) preprocessing
X=df.drop('target',axis=1)
Y=df['target']
X_train,X_test,y_train,y_test=train_test_split(X,Y,random_state=1,test_size=0.2)
Scaler=StandardScaler()
X_train_scaled=Scaler.fit_transform(X_train)
X_test_scaled=Scaler.fit_transform(X_test)

#4) Annotation
iris=load_iris()

df=pd.DataFrame(data=iris.data,columns=iris.feature_names)
df['target']=iris.target

threshold = 2.5
df['is_setosa'] = df['petal length (cm)'] < threshold

# Print the annotated dataset
print(df.head(120))