# -*- coding: utf-8 -*-
"""
Created on Sat May 16 09:18:02 2020

@author: Marcelo Oliveira
"""
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression


# Carregando os dados
base = pd.read_csv('C:/Users/Sara/Documents/GitHub/Curso-Python-Coti/Arquivos_base/cars.csv')

base.head()

# Remover a coluna Unnamed: 0
base = base.drop("Unnamed: 0", axis = 1)

base.head()

# Construção do modelo de regressão linear simples

# Dist -> x
x = base.iloc[:, 1].values
x

# Speed -> y
y = base.iloc[:, 0].values
y

# Correlação
print(np.corrcoef([x,y]))

# Correlação -> o conjunto de x deve estar no formato de uma matriz
x = x.reshape(-1,1)
x


# Criação do modelo de regressão

modelo = LinearRegression()
modelo.fit(x,y)

# Informações

## Interceptação
modelo.intercept_

## Inclinação
modelo.coef_

#Grafico de dispersão
plt.scatter(x,y)
plt.plot(x, modelo.predict(x),color="red")

#prever -> dist 22
modelo.intercept_ + modelo.coef_ *22

#prever -> dist 22
modelo.predict([[22]])
