# -*- coding: utf-8 -*-
"""
Created on Sat May  9 09:17:17 2020

@author: Marcelo Oliveira

"""
ArithmeticError(import os
os.chdir('C:\\Users\\Sara\\Documents\\GitHub\\Curso-Python-Coti') )import os
os.chdir('C:\\Users\\Sara\\Documents\\GitHub\\Curso-Python-Coti') 

import numpy as np

data = np.genfromtxt('Arquivos_base\\iris.data', delimiter=',', usecols=(1,2,3,4))

data

len(data)
data.dtype

data[:50,0]

import matplotlib.pyplot as plt
#%matplotlib inline

plt.plot(data[:50,0], c='Red', ls=':', marker='s', ms='8',
         label='Comp. Sépala Setosa')

plt.plot(data[50:100,0], c='Blue', ls=':', marker='o', ms='8', label='Comp. Sépala Versicolor')


plt.legend()
plt.show()