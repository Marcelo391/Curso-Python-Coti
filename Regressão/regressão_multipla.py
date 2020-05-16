# -*- coding: utf-8 -*-
"""
Created on Sat May 16 09:40:26 2020

@author: Marcelo Oliveira
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression



# Carregando os dados
base = pd.read_csv('../Arquivos_base/mt_cars.csv')

base.head()

# Remover a coluna Unnamed: 0
base = base.drop("Unnamed: 0", axis = 1)

base.head()

# x -> cyl, disp, hp
x = base.iloc[:, 1:4].values
x

# y -> mpg
y = base.iloc[:,0].values
y

# Modelo de regressão multipla
modelo = LinearRegression()

modelo.fit(x,y)

modelo.score(x,y)

#Grafico de dispersão
plt.scatter(x[:,0],y)
plt.scatter(x[:,1],y, color="red")
plt.scatter(x[:,2],y, color="green")


# Registro
registro= np.array([[4, 200, 100]])

modelo.predict(registro)

registro= np.array([[4, 108, 93], [6, 160, 110]])

modelo.predict(registro)


