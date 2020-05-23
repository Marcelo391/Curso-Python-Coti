# -*- coding: utf-8 -*-
"""
Created on Sat May 23 11:23:43 2020

@author: Marcelo Oliveira
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

from sklearn.cluster import KMeans
from sklearn.metrics import confusion_matrix

#Conjunto de dados
from sklearn import datasets

iris = datasets.load_iris()

iris.data
iris.target
iris.target_names

# Retornar o conjunto de dados para cada classe
unicos, quantidade = np.unique(iris.target, return_counts=True)

unicos
quantidade

# Criação do cluster, somente o numero de cluster
cluster = KMeans(n_clusters = 3)
cluster.fit(iris.data)

# Centroide
centroides = cluster.cluster_centers_
centroides

# previsoes
previsoes = cluster.labels_
previsoes


resultado = confusion_matrix(iris.target, previsoes)
resultado


plt.scatter(iris.data[previsoes == 0, 0], iris.data[previsoes == 0, 1],
            c='green', label='Setosa')

plt.scatter(iris.data[previsoes == 1, 0], iris.data[previsoes == 1, 1],
            c='red', label='Versicolor')

plt.scatter(iris.data[previsoes == 2, 0], iris.data[previsoes == 2, 1],
            c='blue', label='Virginica')
