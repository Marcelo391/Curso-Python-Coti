# -*- coding: utf-8 -*-
"""
Created on Sat Jun  6 11:21:56 2020

@author: Marcelo Oliveira
"""

#pip install https://github.com/pybrain/pybrain/archive/0.3.3.zip

from pybrain.structure import FeedForwardNetwork
from pybrain.structure import LinearLayer, SigmoidLayer, BiasUnit
from pybrain.structure import FullConnection


# Construção do objeto rede
rede = FeedForwardNetwork()

# Camada de entrada da rede com 2 neuronios
camadaEntrada = LinearLayer(2)

# Camada oculta com  3 neuronios
camadaOculta = SigmoidLayer(3)

# Camada de saida
camadaSaida = SigmoidLayer(1)

# Unidade de bias
bias1 = BiasUnit()

# Unidade de bias
bias2 = BiasUnit()

# Adicionar os modulos a rede

rede.addModule(camadaEntrada)
rede.addModule(camadaOculta)
rede.addModule(camadaSaida)
rede.addModule(bias1)
rede.addModule(bias2)


# Ligando as camadas

## Ligando camada de entrada com a camada oculta
entradaOculta = FullConnection(camadaEntrada, camadaOculta)

## Ligando camada oculta com a camada de saida
ocultaSaida = FullConnection(camadaOculta, camadaSaida)

# bias oculta
biasOculta = FullConnection(bias1, camadaOculta)

# bias saida
biasSaida = FullConnection(bias2, camadaSaida)

# Ativar a rede
rede.sortModules()

# Ver a construção da rede
print(rede)


print(entradaOculta.params)
print(ocultaSaida.params)
print(biasOculta.params)
print(biasSaida.params)
