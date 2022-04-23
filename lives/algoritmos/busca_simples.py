def gera_lista(tamanho):
    return range(10 ** tamanho)

def busca(n, lista):
    passo = 0
    print(f"Buscando elemento {n} na lista...")
    for i in lista:
        passo += 1
        if i == n:
            print(f"Elemento encontrado em {passo} passos")
            return True
    print(f"Elemento não encontrado ({passo} passos)")
    return False

import sys, time, random
elemento = int(sys.argv[1])
tamanho = int(sys.argv[2])
lista = gera_lista(tamanho)

# Random
elemento = random.randint(0, len(lista))

inicio = time.perf_counter()
busca(elemento, lista)
fim = time.perf_counter()
print(f"Tempo de execução: {fim - inicio}")