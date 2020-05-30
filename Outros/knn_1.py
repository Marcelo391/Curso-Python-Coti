# -*- coding: utf-8 -*-
"""
Created on Sat May 30 10:32:05 2020

@author: Marceloo Oliveira
"""

def load_dados(arquivo):
    amostras = []
    
    with open(arquivo, 'r') as f:
        for linha in f.readlines():
            #[[30,64,1,1], [20,32,1,2]]
            atrib = linha.replace('\n', '').split(',')
            amostras.append([
                int(atrib[0]), int(atrib[1]), int(atrib[2]), int(atrib[3])
                ])
    
    return amostras


amostras = load_dados('C:/Users/Sara/Documents/GitHub/Curso-Python-Coti/Arquivos_base/dataset.data')

amostras


#info_dataset -> Informações sobre o dataset

def info_dataset(amostras, verbose = True):
    
    if verbose:
        print('Total de amostras: %d' % len(amostras))
    
    rotulo1, rotulo2 = 0,0
    
    for amostra in amostras:
        
        if amostra[-1] == 1:
            rotulo1 +=1
        else:
            rotulo2 +=1
            
    if verbose:
        print('Exemplos do rotulo 1: %d' % rotulo1)
        print('Exemplos do rotulo 2: %d' % rotulo2)
        
    return [len(amostras), rotulo1, rotulo2]



# Pegar a quantidade total de cada rótulo
    

_, rotulo1, rotulo2 = info_dataset(amostras)


# Conjunto de treinamento -> 70,30

p =0.7

# Quantidade de registros por grupo
max_rotulo1, max_rotulo2 = int(p*rotulo1), int(p*rotulo2)

print(max_rotulo1)
print(max_rotulo2)

# Criação da função sample
# Separação entre treinamento e teste

treinamento, teste = [], []

def sample(max_r1, max_r2, treinamento, teste, amostras):
    # numero total de amostras por rotulo
    t_r1, t_r2 = 0,0
    
    for amostra in amostras:
        if (t_r1 + t_r2) < (max_r1 + max_r2):
            treinamento.append(amostra)
            if amostra[-1] == 1 and t_r1 < max_r1:
                t_r1 +=1
            else:
                t_r2 +=1
        else:
            teste.append(amostra)

sample(max_rotulo1, max_rotulo2, treinamento, teste, amostras)

info_dataset(treinamento)
info_dataset(teste)


# Criação do KNN

# Distancias

import numpy as np

def dist_euclidiana_np(v1,v2):
    v1, v2 = np.array(v1), np.array(v2)
    diff = v1 - v2
    quad_dist = np.dot(diff, diff)
    return math.sqrt(quad_dist)


# Primeira fase -> calcular a distância em relação a nova amostra
    #213 -> amostras de treinamento
# 213 * 93
    
def knn(treinamento, nova_amostra, K):
    dists, tam_treino = {}, len(treinamento)
    for i in range(tam_treino):
        d = dist_euclidiana_np(treinamento[i], nova_amostra)
        dists[i] = d
    return dists
        

distancias = knn(treinamento, teste[0], 0)
len(distancias)

# Ordenar as distâncias encontradas
sorted(distancias, key=distancias.get)[:5]


# Segunda parte: Selecionar os vizinhos
def knn(treinamento, nova_amostra, K):
    dists, tam_treino = {}, len(treinamento)
    for i in range(tam_treino):
        d = dist_euclidiana_np(treinamento[i], nova_amostra)
        dists[i] = d
        
    # numero de vizinhos
    k_vizinhos = sorted(distancias, key=distancias.get)[:K]
    return k_vizinhos
    

vizinhos = knn(treinamento, teste[0], 5)
print(vizinhos)


# Calculo da votação majoritaria
# 5 -> 3,2 -> nova_instancis -> (3) - primeiro grupo


def knn(treinamento, nova_amostra, K, verbose = True):
    dists, tam_treino = {}, len(treinamento)
    for i in range(tam_treino):
        d = dist_euclidiana_np(treinamento[i], nova_amostra)
        dists[i] = d
        
    # numero de vizinhos
    k_vizinhos = sorted(distancias, key=distancias.get)[:K]
    
    
    if verbose:
        print(k_vizinhos)
    
    #efetuar calculo do voto
        
    qtd_rotulo1, qtd_rotulo2 = 0,0
    
    for indice in k_vizinhos:
        if (treinamento[indice][-1] == 1):
            qtd_rotulo1 +=1
        else:
            qtd_rotulo2 +=1
            
    if verbose:
       print('Rotulo 1: %d ' % qtd_rotulo1)
       print('Rotulo 2: %d ' % qtd_rotulo2)
            
    # Quem ganhou a votação
    if qtd_rotulo1 > qtd_rotulo2:
        return 1
    else:
        return 2
    
    
classe = knn(treinamento, teste[0], 5)
classe

# Definir o numero de vizinhos
# numero de vizinhos -> raiz quadrada do tamanho do treino

def k_n_vizinhos(treinamento):
    n = len(treinamento)
    k = int(math.sqrt(n))
    
    if k % 2 == 0:
        return k+1
    else:
        return  k
    
print(k_n_vizinhos(treinamento))
    

# Criação da função de treinamento
K = k_n_vizinhos(treinamento)

def train(treinamento, teste, K, verbose = False):
    acertos = 0
    for amostra in teste:
        classe = knn(treinamento, amostra, K, verbose)
        if amostra[-1] == classe:
            acertos += 1
    
    return acertos


acertos = train(treinamento, teste, K)
acertos

print('Total de treinamento: %d' % len(treinamento))
print('Total de teste: %d' % len(teste))
print('Total de acertos: %d' % acertos)
print('Porcentagem de acertos: %0.2f%%' % (100 * acertos / len(teste)))







