# -*- coding: utf-8 -*-
"""
Created on Sat May 30 12:31:12 2020

@author: Marcelo Oliveira
"""

from sklearn.neural_network import MLPClassifier
from sklearn import datasets
iris = datasets.load_iris()


entradas = iris.data
saidas = iris.target

# Rede Neural -> Tereinamento

redeNeural = MLPClassifier(verbose = True, max_iter = 1300,
                           tol = 0.00001, learning_rate_init = 0.01 )

redeNeural.fit(entradas, saidas)

# Predição

redeNeural.predict([entradas[120]])
print(saidas[120])


redeNeural.predict([entradas[12]])
print(saidas[12])
