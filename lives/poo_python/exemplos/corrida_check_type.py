from veiculos import Veiculo, Carro, Moto, Bicicleta

class Corrida:
    def __init__(self, veiculos):
        self.veiculos = veiculos

    def iniciar(self):
        for veiculo in self.veiculos:
            if not isinstance(veiculo, Veiculo):
                raise TypeError(f"{veiculo} não é uma instância de Veiculo")
            veiculo.acelerar(3)



carro = Carro("Fusca", 2020, "VW")
moto = Moto("Biz", 2020, "Honda")
bicicleta = Bicicleta()

corrida = Corrida(veiculos=[carro, moto, bicicleta])
corrida.iniciar()