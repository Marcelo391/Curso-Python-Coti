# -*- coding: utf-8 -*-
"""
Created on Sat Jun  6 12:23:33 2020

@author: Marcelo Oliveira
"""

#pip install tensorflow
#pip install keras


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


import keras
#modelo rede sequencial -> feedFowardNetwork
from keras.models import Sequential

# Conectar todos os neuronios da camada
from keras.layers import Dense

# Objeto da rede
classificador = Sequencial()

# Configuração da rede neural
# Camadas ocultas e saida

# 3 + 1 / 2 -> neuronios

# Primeira camada oculta tem que conheçer a quantidade de neuronios na camada de entrada
classificador.add(Dense(units = 2, activation = 'relu', input_dim = 3))
classificador.add(Dense(units = 2, activation = 'relu'))

# Camada de saida
# Problema primario  -> 1
# Resultado da saída -> 0 e 1
classificador.add(Dense(units = 1, activation = 'sigmoid'))

# Executar a rede neural
classificador.compile(optimizer = 'adam', loss = 'binary_crossentropy', metrics = ['accuracy'])

# Treinamento
classificador.fit(previsores_treinamento, classe_treinamento, batch_size = 10, nb_epoch = 100)

previsoes = classificador.predict(previsores_teste)

previsoes = (previsoes > 0.5)

# Cálculo do score
from sklearn.metrics import confusion_matrix, accuracy_score


matriz = confusion_matrix(previsoes, classe_teste)
matriz

precisao = accuracy_score(previsoes, classe_teste)
precisao





