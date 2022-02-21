# Exercícios

1. Escreva um programa que lê números inteiros positivos do usuário, um após o outro, e monta uma lista a partir desses números e depois imprime a lista montada. O programa deve continuar solicitando por números até que o elemento digitado seja um número negativo (que não deve ser inserido na lista).
2. Dada uma lista de números inteiros, escreva um programa que calcula a soma de todos os números na lista.
    
    Se preferir, pode utilizar a lista abaixo como exemplo:
    
    ```python
    lista = [1, 10, 20, 35, 22, 12]
    # Resultado deve ser = 100
    ```
    
3. Data uma lista de números inteiros, escreva um programa que calcula a **média** dos números na lista. O resultado não deve incluir números decimais. Exemplo: `12.3` deve imprimir apenas `12`.
    
    Se preferir, pode utilizar a lista abaixo como exemplo:
    
    ```python
    lista = [1, 10, 20, 35, 22, 12]
    # Resultado deve ser 16
    ```
    
    P.S.: Pode utilizar o operador `//` (divisão inteira)
    
4.  Suponha o seguinte programa:
    
    ```python
    # Alunos e suas respectivas notas
    alunos = [
        ("Alice", 8),
        ("Bob", 7),
        ("Carlos", 9),
    ]
    ```
    
    Escreva uma programa que calcula a média das notas de todos os alunos.
    
5.  Suponha o seguinte programa:
    
    ```python
    # Alunos e suas notas representados através de dicionários
    alunos = [
        {
            "nome": "Alice",
            "nota": 8,
        },
        {
            "nome": "Bob",
            "nota": 7,
        },
        {
            "nome": "Carlos",
            "nota": 9,
        }
    ]
    ```
    
    Escreva uma programa que calcula a média das notas de todos os alunos.
    
6. **DESAFIO**. Escreva um programa que dado uma lista de números inteiros, imprime o maior número dessa lista.
    
    ```python
    lista = [1, 3, 2, 5]
    ...
    # Deve imprimir 5
    ```
    
7. **DESAFIO**. Uma *string* (`str`) também pode ser percorrida utilizando o `for`. 
    
    ```python
    for x in "abc":
        print(x)
    # Vai imprimir:
    # a
    # b
    # c
    ```
    
    Escreva um programa que solicite uma string para o usuário e imprima quantas vezes cada letra aparece na palavra. Por exemplo:
    
    ```python
    "banana"
    # O resultado deve ser
    {
        'a': 3,
        'b': 1,
        'n': 2
    }
    ```
    
8. **DESAFIO.** Escreva um programa que declara uma *lista* com elementos de diferentes tipos e imprime na tela essa lista invertida. **Não é permitido utilizar métodos como `reverse` ou `sort`**.