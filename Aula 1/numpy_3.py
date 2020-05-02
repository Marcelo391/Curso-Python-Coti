# -*- coding: utf-8 -*-
"""
Created on Sat May  2 11:16:24 2020

@author: Marcelo Oliveira
"""

import numpy as np

# Geração de números
array = np.arange(1000000)
print(array)

# Lista do python
#lista = list(range(1000000))
#print(lista)


%time for _ in range(10): array = array * 2
#%time for _ in range(10): lista = [x * 2 for x in lista]

# Array multidimensional
data = np.random.rand(2,3)
print(data)

data.shape
data.dtype
