# -*- coding: utf-8 -*-
"""
Created on Sat May  2 11:01:28 2020

@author: Marcelo Oliveira
"""

import numpy

# Criando um vetor do numpy
a = numpy.array([10,20,30])
print(a)

# Tipo de dado
type(a)

# Matriz 
mat = numpy.array([[1,2], [3,4]])
print(mat)

# Posicao
print(mat[0][0])
print(mat[1][1])

# Imprimir ordem inversa
print(mat[-1][-1])
print(mat[-2][-2])

#Transposta
print(mat.transpose())
