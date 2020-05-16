# -*- coding: utf-8 -*-
"""
Created on Sat May 16 09:59:41 2020

@author: Marcelo Oliveira
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LogisticRegression

base = pd.read_csv('../Arquivos_base/Eleicao.csv', sep=';')
base

# Gráfico
plt.scatter(base.DESPESAS, base.SITUACAO)

# Summary
base.describe()

# Correlação
np.corrcoef(base.DESPESAS, base.SITUACAO)

# X -> despesas
x = base.iloc[:, 2].values
x

# Y -> Situação
y = base.iloc[:, 1].values
y

# Transformar em matriz
x = x[:, np.newaxis]
x

# Criação do modelo de regressão
modelo = LogisticRegression()
modelo.fit(x,y)


# Parâmetros
modelo.coef_
modelo.intercept_


# Carregando os novos candidatos
base_previsoes = pd.read_csv('../Arquivos_base/NovosCandidatos.csv', sep=';')
base_previsoes

despesas = base_previsoes.iloc[:, 1].values

despesas = despesas[:, np.newaxis]
despesas
despesas.shape

previsoes_teste = modelo.predict(despesas)
previsoes_teste

base_previsoes['SITUACAO'] = previsoes_teste
base_previsoes
