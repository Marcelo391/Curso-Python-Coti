# -*- coding: utf-8 -*-
"""
Created on Sat Jun  6 10:47:05 2020

@author: Marcelo Oliveira
"""

import pandas as pd
import numpy as np

base = pd.read_csv('credit_data.csv')

len(base)


# Média dos valores da idade
base.iloc[base.age < 0, 'age'] = 40.92


# Construir os dados -> remover o clienteId

# Previsores -> atributos
previsores = base.iloc[:, 1:4].values

# Classe
classe = base.iloc[:,4].values

from sklearn.impute import SimpleImputer

impute = SimpleImputer(missing_values = np.nan, strategy='mean')

impute = impute.fit(previsores[:, 1:4])

previsores[:, 1:4] = impute.transform(previsores[:, 1:4])

from sklearn.preprocessing import StandardScaler
scaler = StandardScaler()

previsores = scaler.fit_transform(previsores)

from sklearn.model_selection import train_test_split

previsores_treinamento, previsores_teste, classe_treinamento, 
classe_teste =train_test_split(previsores, classe, test_size = 0.25, random_state = 0)


len(previsores_treinamento)
len(previsores_teste)

# Treinamento
from sklearn.neural_network import MLPClassifier

classificador = MLPClassifier(verbose = True, max_iter = 1000, tol = 0.00010, momentum = 0.6)

classificador.fit(previsores_treinamento, classe_treinamento)

previsoes = classificador.predict(previsores_teste)
previsoes

# Cálculo do score
from sklearn.metrics import confusion_matrix, accuracy_score


matriz = confusion_matrix(previsoes, classe_teste)
matriz

precisao = accuracy_score(previsoes, classe_teste)
precisao
