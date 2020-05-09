# -*- coding: utf-8 -*-
"""
Created on Sat May  9 10:48:49 2020

@author: Marcelo Oliveira
"""


import pandas as pd

#pip install db.py
from db import DB

# Carregando os dados do sqlite para o python
database = DB(filename='../Arquivos_base/logs.sqlite3', dbtype='sqlite')

database.tables

# Carregando a tabela
log_df = database.tables.log
log_df

#Carregando com os dados
#Select * from 
lgog_df = database.tables.log.all()
lgog_df

#Query 
log_dfq = database.query('Select * from log where user_id = 3')
log_dfq
