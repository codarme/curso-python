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
        super().__init__()  # Preica
    
    @abstractmethod
    def acelerar(self, intensidade):
        pass


class Carro(Veiculo):
    def __init__(self, modelo, ano, fabricante):
        super().__init__(modelo, ano, fabricante)
        self.portas = {  # Atributo que apenas instâncias de Carro têm.
            0: False,
            1: False,
            2: False,
            3: False,
        }

    def acelerar(self, intensidade):
        print(f"Acelerando carro com intensidade: {intensidade}")
        if self.combustivel <= 0:
            return
        
        if intensidade < 1:  # Não pisou o suficiente no acelerador.
            return
        elif intensidade < 2:
            self.combustivel -= 1
            self.velocidade += 10
        else:  # Intensidade alta.
            self.combustivel -= 2
            self.velocidade += 20

        self.posicao += self.velocidade
        print(f"Nova posição do carro: {self.posicao}")

    def abrir_porta(self, num_porta):  # Específico de carros
        self.portas[num_porta] = True

    def fechar_porta(self, num_porta):  # Específico de carros
        self.portas[num_porta] = False

    @property
    def parado(self):
        # Para quem "usar" a classe Carro sem ver a implementação, não vai saber que "parado" não é um atributo.
        # Inclusive, se tentar fazer "carro.parado = 10", vai receber um erro.
        return self.velocidade == 0

    @property
    def ano(self):
        # Toda vez que carro.ano é acessado, esse método é executado.
        return self._ano  # Por que não simplesmente "return self.ano"?

    @ano.setter
    def ano(self, valor):  
        # Toda vez que fizermos carro.ano = valor, esse método que vai ser chamado.
        if valor > date.today().year:
            return  # Não permite alterar o ano para o futuro.
        self._ano = valor  # Para refletir: por que não fiz "self.ano = valor" (ao invés de "self._ano")


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


class Bicicleta:  # Não herda de veículo, mas tem "acelerar".
    def acelerar(self, intensidade):
        print("Acelerando bicicleta....")
