# -*- coding: utf-8 -*-
"""
Created on Sat May  2 11:27:35 2020

@author: Marcelo Oliveira
"""

import numpy as np

# Lista
l= [10,20,30,40]


# Converte em um array do numpy
a = np.array(l)

# copias -> modo errados
b = a

b[0] = 676432
print(a[0])

# Python -> fatias -> modos errados
c = a[:]

c[0] = 40000
print(a[0])

#  copiar array numpy -> modo correto
d = a.copy()

d[0] = 55

print(a[0])
print(b[0])
print(c[0])
print(d[0])