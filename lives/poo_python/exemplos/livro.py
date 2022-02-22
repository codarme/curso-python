class Pagina:
    def __init__(self, texto):
        self.texto = texto

    def ler(self):
        print(self.texto)

    def __repr__(self) -> str:
        return self.texto

class Livro:
    def __init__(self, paginas):
        self._paginas = paginas  # Lista de páginas
    
    def __getitem__(self, index):
        # Quando fazemos obj[0], o interpretador na verdade faz: obj.__getitem__(0).
        # Logo, podemos fazer qualquer objeto funcionar como uma sequência com índices.
        return self._paginas[index]

    def __len__(self): 
        # O tamanho de um livro (len(livro)) é a quantidade de páginas que ele tem
        return len(self._paginas)

    def ler(self):
        # Ler um livro: ler cada uma de suas páginas em order
        print("Abrindo o livro")
        for p in self._paginas:
            p.ler()
        print("Fechando o livro")


paginas = [
    Pagina("Início"),
    Pagina("Meio"),
    Pagina("Fim"),
]
livro = Livro(paginas=paginas)
livro.ler()
print(f"Primeira página: {livro[0]}")
print(f"Primeiras duas páginas: {livro[0:2]}")
print(f"Tamanho do livro: {len(livro)}")
