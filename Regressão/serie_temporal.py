# -*- coding: utf-8 -*-
"""
Created on Sat May 16 10:21:02 2020

@author: Marcelo Oliveira
"""


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


base = pd.read_csv('../Arquivos_base/AirPassengers.csv')

base.head(10)

print(base.dtypes)

dataparse = lambda dates: pd.datetime.strptime(dates, '%Y-%m')

base = pd.read_csv('../Arquivos_base/AirPassengers.csv',
                   parse_dates=['Month'],
                   index_col='Month',
                   date_parser = dataparse)
base

# Criar uma variável com os dados do base
ts = base['#Passengers']
ts


# Indexação por intervalos
ts['1950-01-01' : '1950-12-01']
ts['1950']

ts.index.max()
ts.index.min()


plt.plot(ts)

# Agrupar os dados
# ano -> A
ts_ano = ts.resample('A').sum()
ts_ano
plt.plot(ts_ano)

ts_datas = ts['1960-01-01' : '1960-12-01']
plt.plot(ts_datas)

# Decomposição da serie temporal
from statsmodels.tsa.seasonal import seasonal_decompose

decomposicao = seasonal_decompose(ts)

# Tendencia
tendencia = decomposicao.trend

# Sazonalidade
sazonal = decomposicao.seasonal

# Efeito aleatorio
aleatorio = decomposicao.resid

# Plotagem dos gráficos

plt.plot(sazonal)
plt.plot(tendencia)
plt.plot(aleatorio)


plt.subplot(4, 1, 1)
plt.plot(ts, label = 'Original')
plt.legend(loc = 'best')

plt.subplot(4, 1, 2)
plt.plot(tendencia, label = 'Tendencia')
plt.legend(loc = 'best')

plt.subplot(4, 1, 3)
plt.plot(sazonal, label = 'Sazonalidade')
plt.legend(loc = 'best')

plt.subplot(4, 1, 4)
plt.plot(aleatorio, label = 'Aleatório')
plt.legend(loc = 'best')

plt.tight_layout()

# Média
ts.mean()

# Média do úlitmo ano
ts['1960-01-01' : '1960-12-01'].mean()

# Média Móvel
media_movel = ts.rolling(window = 12).mean()
media_movel


plt.plot(ts)
plt.plot(media_movel, color='red')

# Previsão do próximo ano
from statsmodels.tsa.arima_model import ARIMA

# Criação do modelo
# order -> 3 parâmetros
# p -> numero de termos auto regressivos
# q -> numero de media model
# d -> numero de diferencas não sazonais
modelo = ARIMA(ts, order = (2, 1, 2))

modelo_treinado = modelo.fit()

modelo_treinado.summary()

previsoes = modelo_treinado.forecast(steps=12)[0]
previsoes

eixo = ts.plot()

modelo_treinado.plot_predict('1960-01-01', '1962-01-01',
                             ax = eixo, plot_insample = True)

# ---------------------------------------------
# Instalar o pyramid
# pip install pyramid
# pip install pmdarima
from pmdarima.arima import auto_arima

modelo_auto = auto_arima(ts, m=12, sessonal=True, trace = True)
modelo_auto.summary()

proximos_12 = modelo_auto.predict(n_periods=12)
proximos_12

from datetime import datetime

test = pd.DataFrame(['1961-01-01', '1961-02-01', '1961-03-01', '1961-04-01', '1961-05-01', 
                               '1961-06-01', '1961-07-01', '1961-08-01' , '1961-09-01' ,'1961-10-01',
                              '1961-11-01', '1961-12-01'], columns = ['datas'] )


previsao  = pd.DataFrame(proximos_12,  columns=['Prediction'])
test.datas
previsao.index = pd.to_datetime(test.datas)
previsao

pd.concat([ts, previsao], axis =1).plot()
