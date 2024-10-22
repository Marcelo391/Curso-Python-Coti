# -*- coding: utf-8 -*-
"""
Created on Sat May 30 10:13:12 2020

@author: Marcelo Oliveira
"""

import math

def dist_euclidiana(v1, v2):
    dim, soma = len(v1), 0
    
    for i in range(dim):
        # Soma da diferença do quadrado de cada elemento do conjunto
        soma += math.pow(v1[i] - v2[i], 2)
        
    return math.sqrt(soma)


v1 = [1.2, 2., 3.8, 4.5]
v2 = [0.5, 4.5, 9.6, 3.4]


print("EX1: %0.2f" % dist_euclidiana(v1, v2))

import numpy as np

def dist_euclidiana_np(v1,v2):
    v1, v2 = np.array(v1), np.array(v2)
    diff = v1 - v2
    quad_dist = np.dot(diff, diff)
    return math.sqrt(quad_dist)


print("EX2: %0.2f" % dist_euclidiana(v1, v2))
