# Exercícios

# Condicionais (if/else/elif)

1. “FizzBuzz” é um problema clássico de programação. O programa recebe um número inteiro e imprime:
    1. “Fizz", caso o número seja múltiplo de 3.
    2. “Buzz", caso o número seja múltiplo de 5.
    3. “FizzBuzz", caso o número seja múltiplo de 3 e de 5.
    
    Por exemplo:
    
    ```python
    3 -> "Fizz" (múltiplo de 3)
    8 -> ... (não imprime nada)
    10 -> "Buzz" (múltiplo de 5)
    15 -> "FizzBuzz" (múltiplo de 3 e 5)
    21 -> "Fizz"
    ```
    
    Implemente o programa *FizzBuzz.*
    
2. Implemente uma calculadora que recebe 3 valores do usuário:
    1. Operando `a` (pode ser um inteiro ou float).
    2. Operando `b` (pode ser um inteiro ou float).
    3. Operador `op`.
        1. `op` pode ser uma *string* representando o operador, por exemplo, `"+"` ou `"-".` Outra opção é utilizar números, por exemplo, `1 para soma`, `2 para subtração`, etc.
    
    O seu programa deve receber esses 3 valores e imprimir o resultado da operação. **Caso o operador seja de divisão e o segundo operando seja o valor zero**, o programa deve imprimir uma mensagem: “Não é possível realizar divisão por zero!”.
    
3. Escreva um programa de autenticação que receba um nome de usuário e senha (`input`) informe se:
    - Autenticação foi bem-sucedida.
    - Se o nome de usuário não existe.
    - Se a senha está incorreta.
    
    Os valores corretos de nome de usuário e senha devem estar armazenados em constantes, como no exemplo abaixo:
    
    ```python
    USUARIO = "admin"
    SENHA = "123123"
    
    nome_usuario = input("Digite o nome do usuário: "\n)
    ...
    ```
    

# Repetição (while)

1. Escreva um programa que receba um número inteiro `n` e imprima a soma de todos os números de 1 até `n` (inclusive `n`).
2. Escreva um programa que receba um número inteiro `n` e imprima *todos os números pares* de 1 até `n` (inclusive `n`).
3. Um número primo é um número que é divisível apenas por 1 e por ele mesmo. Escreva um programa que receba um número `n` e informe se esse número é primo ou não.
4. O jogo “Acerte o número” funciona da seguinte maneira:
    1. Existe um certo número inteiro declarado dentro do programa que o usuário desconhece. Por exemplo: `numero  = 8`
    2. O usuário tem 3 tentativas para acertar o número.
    3. A cada tentativa, é informado ao usuário se o número que ele digitou é maior, menor, ou igual ao número correto.
    4. O jogo termina quando o usuário erra 3 vezes (perdeu) ou quando o usuário acerta o número (ganhou).
    
    Implemente o jogo “Acerte o número”.