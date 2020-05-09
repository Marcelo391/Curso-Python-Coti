# -*- coding: utf-8 -*-
"""
Created on Sat May  2 11:12:22 2020

@author: Marcelo Oliveira
"""

import numpy

#Operações com matrizes
m1 = numpy.array([[1,2],[3,4]])
m2 = numpy.array([[5,6],[7,8]])

print(m1+m2)
print(m1-m2)
print(m1*m2)
print(m1/m2)

m3 = numpy.array([1,2,3,4])
print(m3)

# Somatório
m3.sum()

# indice do elemento que possui o maior valor
m3.argmax()
m3[m3.argmax()]
