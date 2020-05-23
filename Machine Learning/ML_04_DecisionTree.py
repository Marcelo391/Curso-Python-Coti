# -*- coding: utf-8 -*-
"""
Created on Sat May 23 09:49:47 2020

@author: Marcelo Oliveira
"""

import pandas as pd
import numpy as np

from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier

credito = pd.read_csv('../Arquivos_base/Credit.csv')

credito.head
credito.shape

# Dividir o conjunto de credito em dois

#previsores
previsores = credito.iloc[:, 0:20].values

previsores[:2]

#classe
classe = credito.iloc[:, 20].values

classe[:2]

# Efetuar o pre-processamento dos dados
from sklearn.preprocessing import LabelEncoder

labelencoder = LabelEncoder()

previsores[:, 0] = labelencoder.fit_transform(previsores[:, 0])
previsores[:, 2] = labelencoder.fit_transform(previsores[:, 2])
previsores[:, 3] = labelencoder.fit_transform(previsores[:, 3])
previsores[:, 5] = labelencoder.fit_transform(previsores[:, 5])
previsores[:, 6] = labelencoder.fit_transform(previsores[:, 6])
previsores[:, 8] = labelencoder.fit_transform(previsores[:, 8])
previsores[:, 9] = labelencoder.fit_transform(previsores[:, 9])
previsores[:, 11] = labelencoder.fit_transform(previsores[:, 11])
previsores[:, 13] = labelencoder.fit_transform(previsores[:, 13])
previsores[:, 14] = labelencoder.fit_transform(previsores[:, 14])
previsores[:, 16] = labelencoder.fit_transform(previsores[:, 16])
previsores[:, 18] = labelencoder.fit_transform(previsores[:, 18])
previsores[:, 19] = labelencoder.fit_transform(previsores[:, 19])

previsores[0]

# Efetuar o sample -> treinamento 70%, teste 30%

x_treinamento, x_teste, y_treinamento, y_teste = train_test_split(
    previsores, classe, test_size=0.3, random_state = 0)

len(x_treinamento)
len(x_teste)

# Treinamento
arvore = DecisionTreeClassifier(criterion = 'entropy')

arvore.fit(x_treinamento, y_treinamento)


#graphviz
# conda install graphviz
from sklearn.tree import export_graphviz

export_graphviz(
    arvore, 
    out_file='../Arquivos_base/tree.dot',
    feature_names=credito.columns[0:20],
    class_names=credito['class'].unique(),
    leaves_parallel = True, filled = True)

# conda install pydot
import pydot

(graph, ) = pydot.graph_from_dot_file('../Arquivos_base/tree.dot')
graph.write_png('../Arquivos_base/arvore.png')

# Previsoes
previsoes = arvore.predict(x_teste)
previsoes

# Validação / Teste
from sklearn.metrics import confusion_matrix, accuracy_score

matriz = confusion_matrix(previsoes, y_teste)
matriz
precisao = accuracy_score(previsoes, y_teste)
precisao
