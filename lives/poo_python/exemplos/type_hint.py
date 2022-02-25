from typing import Iterable
from veiculos import Veiculo


def soma(a: int, b: int) -> int:
    return a + b

def divisao(a: int, b: int) -> float | int:
    return a / b

class Corrida:
    def __init__(self, veiculos: Iterable[Veiculo]) -> None:
        self.veiculos = veiculos

    def iniciar(self) -> None:
        for veiculo in self.veiculos:
            veiculo.acelerar(3)

            