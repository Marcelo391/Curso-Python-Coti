# -*- coding: utf-8 -*-
"""
Created on Sat May  2 11:47:06 2020

@author: Marcelo Oliveira
"""

import numpy as np

a = np.array([ [1,2], [3,4] ])
a

# Repetind arrays
np.repeat(a, 3)

np.repeat(a, 2, axis = 0)
np.repeat(a, 2, axis = 1)

# tile
np.tile(a, 2)


# Dividindo um array -> split
a = np.array([ [1,2,3], [4,5,6], [7,8,9], [10,11,12] ])

a_sep = np.array_split(a, 4, axis = 0)

for arr in a_sep:
    print(arr)
    
# Arrays de zeros
np.zeros(4)
np.zeros((2,2))

# Arrays de ones
np.ones(4)
np.ones((2,2))

# Array identidade
np.eye(3)

a
# indexação Boleana
a>3

a[ a > 3]


# Juntando uma sequencia de arrays
a = np.array([ [1,2], [3,4] ])
b = np.array([[5,6]])

np.concatenate( (a,b) , axis = 0)

np.concatenate( (a,b.T) , axis = 1)

# Embaralhando uma sequencia
a = np.arange(10)
a

np.random.shuffle(a)
a

# Numeros complex com numpy
a = np.array([ 1, 10 + 2j, 20 + 5j ], dtype=complex)
a

a[1] + a[2]

# Geração de arrays
np.arange(10)
np.arange(1, 100, 2)


#lim spaces
np.linspace(2.0, 3.0, 5)

#Elementos unicos array
a = np.array([[1,2], [2,3], [3,3], [4,4]])
a
np.unique(a)
