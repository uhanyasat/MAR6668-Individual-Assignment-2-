# -*- coding: utf-8 -*-
"""
Created on Wed Oct  6 19:28:49 2021

@author: 
"""

import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
df = pd.read_csv("CoffeeDataStoreB.csv")

print(df.columns)
print(df.describe())


corr = df.corr()
sns.heatmap(corr, xticklabels=corr.columns, yticklabels=corr.columns, annot=True, cmap=sns.diverging_palette(220, 20, as_cmap=True))

sns.pairplot(df)

# Setting X and y variables
X = df.loc[:, df.columns != 'MaxwellSales']
y = df['MaxwellSales']
# Building Random Forest model

from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_absolute_error as mae

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=.25, random_state=0)
model = RandomForestRegressor(random_state=1)
model.fit(X_train, y_train)
pred = model.predict(X_test)
# Visualizing Feature Importance
feat_importances = pd.Series(model.feature_importances_, index=X.columns)
feat_importances.nlargest(25).plot(kind='barh',figsize=(10,10))
print(feat_importances.nlargest(25))