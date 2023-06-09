# -*- coding: utf-8 -*-
"""Design_of_AI_Lab_11.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1kcBsNbJSZ_TNdGuLxk0pgyHIR6199A8U
"""

import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error, r2_score

# Generate sample data
np.random.seed(0)
X = np.random.rand(100, 1)  # Input feature
Y = 2 + 3 * X + np.random.randn(100, 1)  # Target variable

# Split the data into training and test sets
X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.2, random_state=42)

# Create and fit the linear regression model
regression_model = LinearRegression()
regression_model.fit(X_train, Y_train)

# Make predictions on the test set
Y_pred = regression_model.predict(X_test)

# Calculate least squares (mean squared error)
mse = mean_squared_error(Y_test, Y_pred)

# Calculate R-squared score
r2 = r2_score(Y_test, Y_pred)

# Print the results
print("Mean Squared Error:", mse)
print("R-squared Score:", r2)