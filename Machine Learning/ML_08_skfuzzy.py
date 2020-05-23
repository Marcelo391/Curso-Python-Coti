# -*- coding: utf-8 -*-
"""
Created on Sat May 23 11:41:35 2020

@author: marcelo Oliveira
"""

import numpy as np
from sklearn import datasets
from sklearn.metrics import confusion_matrix

# pip install scikit-fuzzy
import skfuzzy


iris = datasets.load_iris()

# Aplicar a transposta na matriz de dados
r = skfuzzy.cmeans(data = iris.data.T, c = 3, m = 2,
                   error = 0.005, maxiter = 1000, init = None)

# Retorna  um tupla -> primeira posição

previsoes_porcentagem = r[1]
previsoes_porcentagem


# 1º Registro
print(previsoes_porcentagem[0][0])
print(previsoes_porcentagem[1][0])
print(previsoes_porcentagem[2][0])


# 2º Registro
print(previsoes_porcentagem[0][1])
print(previsoes_porcentagem[1][1])
print(previsoes_porcentagem[2][1])

r2 = previsoes_porcentagem.T


print(r2[0])
print(r2[1])

# Previsoes
previsoes = previsoes_porcentagem.argmax(axis = 0)
previsoes

confusao = confusion_matrix(previsoes, iris.target)
confusao
