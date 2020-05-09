# -*- coding: utf-8 -*-
"""
Created on Sat May  9 09:47:56 2020

@author: Marcelo Oliveira
"""

import pandas as pd

# COnstruindo dataframes

df = pd.DataFrame([
        ['Python Web', 2000],
        ['Machine Learning', 3000],
        ['lógica de Programação', 2300],
        ['Spark', 2200],
    ], columns=['Cursos', 'Alunos'])

df


df['Cursos']
df['Alunos'].describe()
