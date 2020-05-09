# -*- coding: utf-8 -*-
"""
Created on Sat May  9 09:37:37 2020

@author: Marcelo Oliveira
"""
import numpy as np
import pandas as pd

# Series -> dados em uma unica dimensao
s = pd.Series([1,4,5,6,7,10,6])

s

# Posição
s[0]

#Fatias 
s[0:2]


# Describe -> summary
s.describe()

# Media
s.mean()

# Duplicados
s.duplicated()

# Juntando series
s2 = pd.Series([11,5,8])
s.append(s2)
