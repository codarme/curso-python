from abc import ABC, abstractmethod
from datetime import date
from typing import Type



class Veiculo(ABC):
    def __init__(self, modelo, ano, fabricante):
        self.modelo = modelo
        self._ano = ano
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
        if not self.combustivel > 0:
            return

        if intensidade == 1:
            self.combustivel -= 1
            self.velocidade += 10
        elif intensidade == 2:
            self.combustivel -= 2
            self.velocidade == 20
        elif intensidade == 3:
            self.combustivel -= 3
            self.velocidade == 30
        else:
            return

        self.posicao += self.velocidade

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
        if valor > date.today().ano:
            return
        self.ano = valor


class Moto(Veiculo):
    pass


class Bicicleta:  # Não herda de veículo, mas tem "acelerar"
    def acelerar(self, intensidade):
        print("Acelerando bicicleta....")

