# -*- coding: utf-8 -*-
"""
Created on Sat May 16 11:53:58 2020

@author: Marcelo Oliveira
"""

import pandas as pd
import numpy as np

from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import GaussianNB

credito = pd.read_csv('../Arquivos_base/Credit.csv')
credito

len(credito)
credito.shape

credito.columns

# previsores -> atributos
previsores = credito.iloc[:, 0:20].values

#classe -> alvo
classe = credito.iloc[:, 20].values

classe
previsores[:2]


# pré-processamento
credito['checking_status'].unique()

from sklearn.preprocessing import LabelEncoder

labelenconder = LabelEncoder()

previsores[:, 0] = labelenconder.fit_transform(previsores[:, 0])
previsores[:, 2] = labelenconder.fit_transform(previsores[:, 2])
previsores[:, 3] = labelenconder.fit_transform(previsores[:, 3])
previsores[:, 5] = labelenconder.fit_transform(previsores[:, 5])
previsores[:, 6] = labelenconder.fit_transform(previsores[:, 6])
previsores[:, 8] = labelenconder.fit_transform(previsores[:, 8])
previsores[:, 9] = labelenconder.fit_transform(previsores[:, 9])
previsores[:, 11] = labelenconder.fit_transform(previsores[:, 11])
previsores[:, 13] = labelenconder.fit_transform(previsores[:, 13])
previsores[:, 14] = labelenconder.fit_transform(previsores[:, 14])
previsores[:, 16] = labelenconder.fit_transform(previsores[:, 16])
previsores[:, 18] = labelenconder.fit_transform(previsores[:, 18])
previsores[:, 19] = labelenconder.fit_transform(previsores[:, 19])

previsores[:1]


# Efetuar o sample -> Treinamento 70%, teste 30%

x_treinamento, x_teste, y_treinamento, y_teste = train_test_split(
    previsores, classe, test_size=0.3, random_state=0)

# Criação do Naive Bayes
naive = GaussianNB()

# Treinamento
naive.fit(x_treinamento, y_treinamento)

# Previsões
previsoes = naive.predict(x_teste)
previsoes

from sklearn.metrics import confusion_matrix, accuracy_score
matriz = confusion_matrix(previsoes, y_teste)
matriz

#  calculo manual
acertos = matriz[0][0] + matriz[1,1]
precisao = acertos / matriz.sum()
precisao

# calculo com accuracy_score
precisao = accuracy_score(previsoes, y_teste)
precisao
