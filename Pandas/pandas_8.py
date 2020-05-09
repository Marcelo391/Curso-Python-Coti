# -*- coding: utf-8 -*-
"""
Created on Sat May  9 11:18:33 2020

@author: Marcelo Oliveira
"""

import pandas as pd
import numpy as np

df = pd.read_csv('../Arquivos_base/primary-results.csv')

df.head()

#Groupby -> agrupando dados
dfg =df.groupby('candidate').aggregate(
    {'votes': [np.min, np.mean, np.max] })

dfg

dfg2 =df.groupby('candidate').aggregate(
    {'votes': np.max,
     'fraction_votes': np.max})


# Melhor votes -> Candidato fraction votes = 1
 df[  (df['fraction_votes'] == 1) & 
    (df['candidate'] == 'Hillary Clinton') ]
 
 # Agrupamento
t = df.groupby(['state_abbreviation', 'candidate'])['votes'].sum()


