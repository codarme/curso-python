from abc import ABC, abstractmethod
from datetime import date
from typing import Type

from veiculos import Carro, Moto, Veiculo, Bicicleta


class Corrida:
    def __init__(self, veiculos):
        self.veiculos = veiculos

    def iniciar(self):
        for veiculo in self.veiculos:
            veiculo.acelerar(3)



carro = Carro("Fusca", 2020, "VW")
moto = Moto("Biz", 2020, "Honda")

# Bicicleta não É um veículo, mas se comporta como um pois tem o método acelerar
# "se anda que nem um pato, faz quack que nem um pato..."
bicicleta = Bicicleta()  

corrida = Corrida(veiculos=[carro, moto, bicicleta])
corrida.iniciar()