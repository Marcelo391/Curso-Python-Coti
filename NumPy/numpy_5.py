# -*- coding: utf-8 -*-
"""
Created on Sat May  2 11:33:57 2020

@author: Marcelo Oliveira
"""

import numpy as np

# Inserindo dados no array
arr = np.array([1,2,3])
print(arr)

np.insert(arr, 1, 10)
print(arr)

a = np.array([[1,2,3],[4,5,6]])
a

# Coluna
np.insert(a, 1, 5, axis = 1)

# Linha
np.insert(a, 1, 5, axis = 0)

# Somatorio
a.sum()

# Axis -> eixos
a.sum(axis = 0)
a.sum(axis = 1)

# Append
a1 = np.array([1,2,3])
a1

# Juntar arrays
np.append(a1, [4,5,6])

a = np.array([[1,2],[3,4]])
a

np.append(a, [[5,6]], axis = 0)

np.append(a, ([[5],[6]]), axis = 1)










