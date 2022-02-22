from dataclasses import dataclass


@dataclass(frozen=True)  # Imutável
class Ponto:
    x: int
    y: int


p = Ponto(0, 2)
p.x = 10  # Erro: os atributos de Ponto são imutáveis!