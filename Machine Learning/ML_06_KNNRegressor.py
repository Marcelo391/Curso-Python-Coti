# -*- coding: utf-8 -*-
"""
Created on Sat May 23 11:01:07 2020

@author: Marcelo Oliveira
"""

from sklearn.datasets import load_boston

boston = load_boston()
type(boston)

#dimensoes
boston.data.shape

help(boston)

# feature_names -> atributos
boston.feature_names

from sklearn.neighbors import KNeighborsRegressor
from sklearn.model_selection import train_test_split

K = 9
knn = KNeighborsRegressor(n_neighbors = K)

knn.fit(boston.data, boston.target)

print(boston.target[0])


print(knn.predict([boston.data[0]]))

# Treinar 50 instancias

x, y = boston.data[:50], boston.target[:50]
x
y

y_ = knn.fit(x, y).predict(x)
y_

import matplotlib.pyplot as plt
import numpy as np


plt.plot(np.linspace(-1, 1, 50), y, label='data', color='black')
plt.plot(np.linspace(-1, 1, 50), y_, label='prediction', color='red')
plt.legend()
plt.show()


from sklearn.metrics import mean_squared_error
mean_squared_error(boston.target[:50], y_)