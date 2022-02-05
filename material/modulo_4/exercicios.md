# Exercícios

1. Escreva um programa que receba um número inteiro do usuário e imprima *True* caso o número seja *par* e *False*, caso o número seja ímpar.
2. O que vai ser impresso na tela ao executar o programa abaixo? (são 2 `prints`!)
    
    ```python
    a = 5
    b = 10
    x = True
    y = False
    
    print((x or y) and (a < b))
    print((x or y) and not (a < b))
    ```
    
    Execute o código e verifique se você acertou 😄
    
3. Considere o programa abaixo
    
    ```python
    resultado = 2 + 3 * 2 ** 2
    print(resultado)
    ```
    
    É possível conseguir resultados diferentes, sem alterar os números e operadores, apenas com a utilização de **parênteses**. Por exemplo:
    
    ```python
    resultado = (2 + 3) * 2 ** 2
    print(resultado)
    # 20
    ```
    
    Utilize parênteses de modo que o programa imprima os seguintes resultados:
    
    - 14
    - 38
    - 100
4. Alice é responsável por escrever um programa que verifica se um cupom de desconto pode ser utilizado. O programa recebe 3 valores e retorna `True` caso o cupom possa ser utilizado, ou `False`, caso contrário.
    
    Os três valores que o programa recebe são:
    
    1. Valor de compra (*float*)
    2. Valor do frete (*float*)
    3. Cliente é cadastrado no programa de fidelidade (*string “s” (sim) ou “n” (não)*)
    
    O cupom tem a seguinte regra:
    
    > Caso o valor da compra somado ao frete seja superior a **R$ 100**, ou o cliente seja cadastrado no programa de fidelidade, o cupom de desconto pode ser utilizado. Caso contrário, o cupom não pode ser utilizado.
    
    Seu objetivo é implementar o programa que atenda a especificação acima.