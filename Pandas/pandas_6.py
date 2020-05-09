# -*- coding: utf-8 -*-
"""
Created on Sat May  9 10:59:49 2020

@author: Marcelo Oliveira
"""

import pandas as pd
import pydataset

titanic = pydataset.data('titanic')

titanic.head(5)

#colunas
titanic.columns

# Class -> bytes
titanic['class'].nbytes

# Transformar em dados categoricos pandas
titanic['class'] = titanic['class'].astype('category')


# Class -> bytes
titanic['class'].nbytes


