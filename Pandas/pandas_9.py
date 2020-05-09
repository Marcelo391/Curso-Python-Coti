# -*- coding: utf-8 -*-
"""
Created on Sat May  9 11:38:58 2020

@author: Marcelo Oliveira
"""

import pandas as pd
import numpy as np

df = pd.read_csv('../Arquivos_base/primary-results.csv')

df.head()

#Candidatos da campanha
df['candidate'].unique()


# PIVOT -> pivotagem, reorganização de dados tabulates

dfp = pd.pivot_table(df, index = ['state', 'party','candidate'],
               values =['votes'], aggfunc={'votes': np.sum})


# Ranking -> soma dos votos por distritos

df['rank'] = df.groupby(['county', 'party'])['votes'].rank(ascending=False)
df['rank2'] = df.groupby(['county', 'party'])['votes'].rank(ascending=True)

del df['rank2']


# Agrupar por estado, partido, candidato
dfg = df.groupby(['state', 'party','candidate']).sum()

del dfg['fraction_votes']
del dfg['fips']

dfg

dfg.reset_index(inplace = True)

dfg.head(10)

dfg['rank'] = dfg.groupby(['state','party'])['votes'].rank(ascending = False)
dfg.head(10)

# Pivot
pd.pivot_table(dfg, index=['state','party','candidate'],
               values=['rank','votes'])


dfs = dfg.sort_values(['state','party','votes'])