class Evento:
    CATEGORIAS = [
        "Backend",
        "Frontend",
        "Fullstack",
        "UX/UI",
    ]

    def __init__(self, nome, categoria, local=None, link=None):
        if not categoria in Evento.CATEGORIAS:
            raise ValueError(f"Categoria {categoria} inexistente. Opções: {Evento.CATEGORIAS}")
        self.nome = nome
        self.categoria = categoria
        self.local = local
        self.link = link