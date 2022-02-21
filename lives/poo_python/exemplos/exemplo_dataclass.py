from dataclasses import dataclass

@dataclass
class Carro:
    modelo: str
    ano: int
    fabricante: str
    posicao = 0
    velocidade = 0
    combustivel = 0
