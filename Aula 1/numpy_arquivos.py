# -*- coding: utf-8 -*-
"""
Created on Sat May  2 12:15:41 2020

@author: Marcelo Oliveira
"""

import numpy as np

# Arquivos com numpy


val1, val2, val3 = np.loadtxt('../Arquivos_base/dados.txt', skiprows = 1,
                              unpack = True)

val1
val2
val3

my_array = np.genfromtxt('../Arquivos_base/dados2.txt',
                         skip_header = 1,
                         filling_values = 1000)

my_array


# Lendo do CSV -> arquivo em formato de tabela

valores = np.genfromtxt('../Arquivos_base/arquivo.csv', delimiter = ';',
                        skip_header = 1)

valores
