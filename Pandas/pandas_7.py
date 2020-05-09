# -*- coding: utf-8 -*-
"""
Created on Sat May  9 11:05:14 2020

@author: Marcelo de Oliveira
"""

import pandas as pd
import pydataset

copacabana = pd.read_csv('../Arquivos_base/copacabana_lat_lng.csv')


copacabana.describe()

# Comparação -> indexação boleana
copacabana['Quartos'] > 3
(copacabana['Quartos'] > 3) & (copacabana['DistFavela'] > 700)

copacabana[ (copacabana['Quartos'] > 5 )]
copacabana[ (copacabana['Quartos'] > 3) & (copacabana['DistFavela'] > 700) ]

# Construir colunas
copacabana['Valor Total'] = copacabana['AreaConstruida'] * copacabana['VAL_UNIT']
copacabana['Valor Total']

