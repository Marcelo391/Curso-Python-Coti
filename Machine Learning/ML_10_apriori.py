# -*- coding: utf-8 -*-
"""
Created on Sat May 23 12:10:33 2020

@author: Marcelo Oliveira

 ----INCOMPLETO -----
"""


import pandas as pd

# pip install apyori
from apyori import apriori

dados = pd.read_csv('../Arquivos_base/mercado2.csv', header = None)

dados.head()
qtdDados = len(dados)
qtdColunas = len(dados.columns)

# Transformar em uma transação
#[ [pao, cafe, leite]],
#  [biscoito, cafe, copo]]

transacoes = []

for i in range(qtdDados):
    transacoes.append([
        str(dados.values[i,j]) for j in range(qtdColunas) ])


transacoes = [0]
transacoes = [:2]

# Associação 

regras = apriori ( transacoes, min_support = 0.003, min_)

