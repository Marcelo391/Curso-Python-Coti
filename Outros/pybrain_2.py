# -*- coding: utf-8 -*-
"""
Created on Sat Jun  6 11:51:37 2020

@author: Marcelo Oliveira
"""

from pybrain.tools.shortcuts import buildNetwork
from pybrain.datasets import SupervisedDataSet
from pybrain.supervised.trainers import BackpropTrainer

from pybrain.structure.modules import SoftmaxLayer
from pybrain.structure.modules import SigmoidLayer

# Camaca de entrada 2
# Camaca de oculta 3
# Camaca de sasida 1

rede = buildNetwork(2, 3, 1)

#logs

print(rede['in'])
print(rede['hidden0'])
print(rede['out'])

# Mudar a camada de saida para softmaxLayer
rede = buildNetwork(2, 3, 1, outclass = SigmoidLayer, hiddenclass = SigmoidLayer)

print(rede['out'])

# Construção do dataset
# Dois atributos e uma classe
base = SupervisedDataSet(2, 1)

# Operador XOR ->

base.addSample(((0,0)), ((0,)))
base.addSample(((0,1)), ((1,)))
base.addSample(((1,0)), ((1,)))
base.addSample(((1,1)), ((0,)))

print(base['input'])
print(base['target'])

# Treinamento
treinamento = BackpropTrainer(rede, dataset = base, learningrate = 0.01, momentum = 0.6)


# Simular as épocas
for i in range(1, 30000):
    erro = treinamento.train()
    if i % 1000 == 0:
        print('Erro: %s' %erro)
        
  
# Testar a rede neural
print(rede.activate([0,0]))    
print(rede.activate([0,1]))    
print(rede.activate([1,0]))    
print(rede.activate([1,1]))    
        
        