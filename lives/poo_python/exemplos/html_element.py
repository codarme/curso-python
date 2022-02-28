from abc import ABC, abstractmethod


class HTMLElement(ABC):
    @abstractmethod
    def onHover(self):
        pass

    @abstractmethod
    def onClick(self):
        pass


class Button(HTMLElement):
    def onHover(self):
        print("Mouse em cima do botão!")

    def onClick(self):
        print("Clicou no botão")


class Link(HTMLElement):
    def __init__(self) -> None:
        self.cor_link = "azul"
        self.link_clicado = False
        super().__init__()

    def onHover(self):
        self.cor_link = "verde"
        print("Alterar cor do link")

    def onClick(self):
        print("Link clicado")
        self.link_clicado = True
        self.cor_link = "roxo"