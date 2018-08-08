# -*- coding: utf-8 -*-
"""
@author: Vijay Manda
"""

# DATA PREPROCESSING
# Replace null values with mean of column and encode categorical data

# import necessary libraries
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# load data from csv file
dataset = pd.read_csv('Data.csv')

# data contains four columns - Country, Age, Salary and Purchased
# Country, Age and Salary are independent variables or features
# Purchased is the dependent variable
X = dataset.iloc[:, :-1].values
y = dataset.iloc[:, 3].values

# We have to clean up the data before we can use it

# Replace missing values by mean of values of columns
# Imputer is a Imputation transformer for completing missing values.
from sklearn.preprocessing import Imputer
imputer = Imputer(missing_values='NaN', strategy='mean', axis=0)
imputer = imputer.fit(X[:,1:3])
X[:,1:3] = imputer.transform(X[:, 1:3])

# Categorical values
from sklearn.preprocessing import LabelEncoder
labelencoder_x = LabelEncoder()
X[:,0] = labelencoder_x.fit_transform(X[:,0])

# Encode categorical data
from sklearn.preprocessing import OneHotEncoder
onehotencoder = OneHotEncoder(categorical_features=[0])
X = onehotencoder.fit_transform(X).toarray()

labelencoder_y = LabelEncoder()
y = labelencoder_y.fit_transform(y)
