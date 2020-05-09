# -*- coding: utf-8 -*-
"""
Created on Sat May  9 12:10:32 2020

@author: Marcelo Oliveira
"""

import pandas as pd
from db import DemoDB

#DemoDB -> banco de dados de exmplos
database = DemoDB()

database.tables

album = database.tables.Album.all()
artist = database.tables.Artist.all()

#Juntando os dataframes de album e artista
#campo id do artista
album_artist = pd.merge(artist, album)

#Especificando o campo
album_artist = pd.merge(artist, album, on="ArtistId")

#E se as colunas fossem diferentes ?

#Renomeando as colunas do data frame
album.rename(columns={'ArtistId': 'Artist_Id'}, inplace = True)

#Especificando os dois campos
album_artist = pd.merge(artist, album, left_on="ArtistId",
                        right_on="Artist_Id").drop('Artist_Id', axis=1)


# Conjunto de dados de vendas
# Unir os dados

vendas1 = pd.DataFrame(
        {
            'nome': ['Lucas', 'Vinicius'],
            'codigo': [10,20],
        }
    )


vendas2 = pd.DataFrame(
        {
            'nome': ['Ana', 'Vinicius', 'Joana'],
            'valor': [5000,3500, 2020],
        }
    )


vendas_inner = pd.merge(vendas1, vendas2, on="nome", how="inner")
vendas_left = pd.merge(vendas1, vendas2, on="nome", how="left")
vendas_right = pd.merge(vendas1, vendas2, on="nome", how="right")
vendas_outer = pd.merge(vendas1, vendas2, on="nome", how="outer")







