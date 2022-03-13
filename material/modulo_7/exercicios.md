# Exercícios

1. Escreva uma função que recebe um número inteiro positivo e retorna `True` caso ele seja primo e `False`, caso contrário.
    
    Sugestão:
    
    ```python
    def e_primo(n):
        # Sua implementação aqui
    
    print(e_primo(1))
    # False
    print(e_primo(2))
    # True
    ```
    
2. Implemente uma função que recebe uma *lista* de números inteiros e retorna uma ***tupla*** `(pos, num)`, onde `pos` é a posição (ou índice) do maior número na lista e `num` é o valor desse número.
3. Implemente uma função `maior_idade(pessoa)` que receba uma *tupla* representando uma pessoa com nome e idade e imprime na tela se a pessoa é maior de idade ou não.
4. Adapte a função `maior_idade(pessoa)` de forma que ela possa receber tanto uma *tupla* quanto um *dicionário*. Dica: método `type` pode te ajudar.
5. Implemente uma função que recebe dois argumentos, uma `lista` e um `elemento`, e retorna `True` caso `elemento` seja encontrado na `lista`, e `False` caso contrário.
6. **DESAFIO**. Uma função fatorial calcula o valor da multiplicação de um certo número inteiro não-negativo por todos os números positivos menores que ele. A exceção é o fatorial de **zero** que é igual a **1.** Por exemplo:
    
    ```python
    fatorial(3) = 3 * 2 * 1 = 6
    fatorial(1) = 1
    fatorial(0) = 1
    ```
    
    Ou seja, podemos definir a função fatorial como:
    
    ```python
    fatorial(n) = n * n-1 * n-2 * ... * 1
    ```
    
    Implemente a função `fatorial(n)` de modo que ela retorne o valor do fatorial de n.
