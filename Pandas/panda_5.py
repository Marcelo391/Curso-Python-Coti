# -*- coding: utf-8 -*-
"""
Created on Sat May  9 10:24:19 2020

@author: Marcelo Oliveira
"""

import pandas as pd
import numpy as np


populacao = pd.read_excel('../Arquivos_base/total-populacao-pernambuco.xls')

populacao.head()

# Exibir o total de mulheres
populacao['Total de mulheres']

sum(populacao['Total de mulheres'][:-1])
populacao['Total de mulheres'].sum()

relhm = populacao['Total de mulheres'] / populacao['Total de homens']

#min
min(relhm)


# Adicionar ao dataframe
populacao['rhm'] = relhm


# Qual cidade tem o minimo e o maximo ?
# Indexação de booleano

pmin = populacao[ populacao['rhm'] ==  min(populacao['rhm'])]
pmax = populacao[ populacao['rhm'] ==  max(populacao['rhm'])]
