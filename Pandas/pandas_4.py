# -*- coding: utf-8 -*-
"""
Created on Sat May  9 10:14:45 2020

@author: Marcelo Oliveira
"""

import pandas as pd

#pip install pydataset -> Anaconda Prompt
#base
import pydataset

#conjunto de dados padrao de um dataframe
pydataset.data()


len(pydataset.data())
type(pydataset.data())

# Carregando um dataset
titanic = pydataset.data('titanic')

titanic.head()
titanic.tail()

# Cntagem
titanic['class'].value_counts()
titanic['sex'].value_counts()
titanic['age'].value_counts()
titanic['survived'].value_counts()
