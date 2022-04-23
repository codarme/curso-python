def gera_lista(tamanho):
    return range(10 ** tamanho)

def busca_binaria(n, lista):
    passo = 0
    inicio = 0
    fim = len(lista) - 1

    while inicio <= fim:
        passo += 1
        meio = (inicio + fim) // 2
        chute = lista[meio]

        if chute == n:
            return True
        if chute > n:
            fim = meio - 1
        else:
            inicio = meio + 1


import sys, time, random, timeit
elemento = int(sys.argv[1])
tamanho = int(sys.argv[2])
lista = gera_lista(tamanho)

def run():
    elemento = random.randint(0, len(lista))
    busca_binaria(elemento, lista)

import timeit
print(timeit.timeit("run()", setup="from __main__ import run", number=1000))