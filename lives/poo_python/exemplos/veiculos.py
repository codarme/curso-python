from abc import ABC, abstractmethod
from datetime import date
from typing import Type



class Veiculo(ABC):
    def __init__(self, modelo, ano, fabricante):
        self.modelo = modelo
        self.ano = ano
        self.fabricante = fabricante
        self.posicao = 0
        self.velocidade = 0
        self.combustivel = 0
        super().__init__()
    
    @abstractmethod
    def acelerar(self, intensidade):
        pass


class Carro(Veiculo):
    def __init__(self, modelo, ano, fabricante):
        super().__init__(modelo, ano, fabricante)
        self.portas = {
            0: False,
            1: False,
            2: False,
            3: False,
        }

    def acelerar(self, intensidade):
        print(f"Acelerando carro com intensidade: {intensidade}")
        if self.combustivel <= 0:
            return
        
        if intensidade < 1:  # Não pisou o suficiente no acelerador
            return
        elif intensidade < 2:
            self.combustivel -= 1
            self.velocidade += 10
        else:  # Intensidade alta
            self.combustivel -= 2
            self.velocidade += 20

        self.posicao += self.velocidade
        print(f"Nova posição do carro: {self.posicao}")

    def abrir_porta(self, num_porta):
        self.portas[num_porta] = True

    def fechar_porta(self, num_porta):
        self.portas[num_porta] = False

    @property
    def parado(self):
        return self.velocidade == 0

    @property
    def ano(self):
        return self._ano

    @ano.setter
    def ano(self, valor):
        if valor > date.today().year:
            return
        self._ano = valor


class Moto(Veiculo):
    def acelerar(self, intensidade):
        print(f"Acelerando moto com intensidade: {intensidade}")
        if self.combustivel <= 0:
            return

        if intensidade < 1:
            return

        if intensidade < 2:
            self.combustivel -= 0.5  # Gasta menos que um carro!
            self.velocidade += 20  # Acelera mais que o carro!
        else:  # Só tem duas intensidades
            self.combustivel -= 1
            self.velocidade += 40

        self.posicao += self.velocidade
        print(f"Nova posição da moto: {self.posicao}")


class Bicicleta:  # Não herda de veículo, mas tem "acelerar"
    def acelerar(self, intensidade):
        print("Acelerando bicicleta....")
