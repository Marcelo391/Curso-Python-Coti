# -*- coding: utf-8 -*-
"""
Created on Sat May  9 10:00:47 2020

@author: Marcelo Oliveira
"""

import pandas as pd

df = pd.DataFrame([
    ['PE','Pernambuco','Recife'],
    ['SP','São Paulo','São Paulo'],
    ['RJ','Rio de Janeiro','Rio de Janeiro'],
    ['PB','Paraiba','João Pessoa'],
    ['CE','Ceara','Fortaleza'],
    ['MG','Minas Gerais','Belo Horizonte'],

], columns = ['Sigla', 'Nome', 'Capital'])


df
df['Sigla']

# indice do datafram
df.index

# Iloc
df.iloc[0]
# Fatia
df.iloc[0:2]

# Loc
df.loc[0]
# Fatia
df.loc[0:2]


# Sustituir o indice do dataFrame
df.index = df['Sigla']
df

# Remover a sigla
del df['Sigla']

df


# Varrer
df['SP': 'MG']

df[: 'CE']

