# Programação orientada a objetos com Python (POOP)


## Revisão
* Definindo classes
* Instanciando objetos
* Atributos
  * Atributos de classe
  * Atributos de instância
* Métodos
  * Instância
  * *classmethod*
  * *staticmethod*
* Construtor
  * Python: *inicialização vs criação*
    * `__init__` vs `__new__`
* Herança
  * Sobrescrita de métodos
  * Sobrescrita de construtor
    * Precisa invocar o construtor da classe-mãe
    * `super()`
* Mutabilidade e Imutabilidade
  * Tipos definidos pelo usuário são mutáveis por padrão

## Conceitos gerais de POO
* Encapsulamento
  * Encapsular estado e comportamento.
  * Modificadores de acesso: `public` vs `private`
  * Getters vs setters
* Abstração
  * Estruturas de dados (`dict`)
  * Métodos (`print`)
  * Classes e objetos
* Herança
  * Herança múltipla
* Polimorfismo
  * Interface
  * Duck typing
* Associação
* Agregação
* Composição
  * Composição vs Herança

## Encapsulamento

```python
```

```python
```

### Modificadores de acesso

```python
class Ordem:
    def __init__(valor, método_pagamento = "Crédito")
        self.valor = valor
        self.método_pagamento = método_pagamento
        self.__moeda = "BRL"

    def pagar(self):
        if self.método == "Boleto":
            boleto = self.__gerar_boleto(valor)
            self.__enviar_boleto_email(boleto)
            return "Boleto enviado"
        ...
```

## Abstração
* Esconder detalhes de implementação

## Herança

## Polimorfismo

# Referências
* https://python-course.eu/oop/properties-vs-getters-and-setters.php