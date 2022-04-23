def gera_lista(tamanho):
    return range(10 ** tamanho)

def busca_binaria(n, lista):
    print(f"Buscando elemento {n} na lista...")
    passo = 0
    inicio = 0
    fim = len(lista) - 1

    print(f"Tamanho lista: {len(lista)}")
    while inicio <= fim:
        passo += 1
        print(f"passo: {passo}")
        print(f"inicio: {inicio}")
        print(f"fim: {fim}")
        meio = (inicio + fim) // 2
        chute = lista[meio]

        print(f"Chute: {chute}")
        if chute == n:
            print(f"Elemento encontrado em {passo} passos")
            return True
        if chute > n:
            fim = meio - 1
        else:
            inicio = meio + 1
        print("------")
    print(f"Elemento não encontrado em {passo} passos.")


import sys, time, random
elemento = int(sys.argv[1])
tamanho = int(sys.argv[2])
lista = gera_lista(tamanho)

# Random
elemento = random.randint(0, len(lista))

inicio = time.perf_counter()
busca_binaria(elemento, lista)
fim = time.perf_counter()
print(f"Tempo de execução: {fim - inicio}")