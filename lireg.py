# -*- coding: utf-8 -*-
"""LiREG.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/18iXC4met3zCXT1Ctwoel5AQ48sS6u1u_
"""

# Commented out IPython magic to ensure Python compatibility.
from google.colab import files
import pandas as pd
import os
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# %matplotlib inline

# Use the file picker to select the file
uploaded = files.upload()

# Get the first key from the uploaded dictionary
file_name = list(uploaded.keys())[0]

# Read the CSV file into a DataFrame
HouseDF = pd.read_csv(file_name)

# Display the first few rows of the DataFrame
print(HouseDF.head())

HouseDF.info()

HouseDF.describe()

HouseDF.columns

sns.pairplot(HouseDF)

sns.heatmap(HouseDF.corr(), annot=True)

X = HouseDF[['Avg. Area Income', 'Avg. Area House Age', 'Avg. Area Number of Rooms',
             'Avg. Area Number of Bedrooms', 'Area Population']]

Y = HouseDF['Price']

from sklearn.model_selection import train_test_split

X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size = 0.40, random_state = 101)

from sklearn.linear_model import LinearRegression

lm = LinearRegression()

lm.fit(X_train, Y_train)

coeff_df = pd.DataFrame(lm.coef_, X.columns, columns = ['Coefficient'])

coeff_df

predictions = lm.predict(X_test)

plt.scatter(Y_test, predictions)

sns.distplot((Y_test-predictions), bins = 50);