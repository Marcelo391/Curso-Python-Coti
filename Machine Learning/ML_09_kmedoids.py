# -*- coding: utf-8 -*-
"""
Created on Sat May 23 11:56:02 2020

@author: Marcelo Oliveira
"""


import numpy as np
import pandas as pd
from sklearn import datasets
from sklearn.metrics import confusion_matrix

# pip install pyclustering
from pyclustering.cluster.kmedoids import kmedoids
from pyclustering.cluster import cluster_visualizer


iris = datasets.load_iris()

# Somente duas colunas do conjunto de dados
# indices dos medois [3, 12, 20]
cluster = kmedoids(iris.data[:, 0:2], [3, 12, 20])
cluster

# Medoids
cluster.get_medoids()

# efetuar o agrupamento
cluster.process()

previsoes = cluster.get_clusters()
previsoes

previsoes[0]
previsoes[1]

# Medoids
medoids = cluster.get_medoids()
medoids

len(previsoes[2])

# Efetuar a visualização
v = cluster_visualizer()
v.append_clusters(previsoes, iris.data[:, 0:2])
v.append_cluster(medoids, iris.data[:, 0:2],
                 marker='*', markersize = 10)
v.show()