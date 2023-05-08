# Exercícios

Implemente um sistema com as seguintes especificações:
1. Módulo `usuario.py`
    1. Deve conter uma classe `Usuario`
    2. Classe `Usuario` deve ter um construtor que recebe `nome` e `email`
    3. Classe `Usuario` deve possuir um *método de instância* `imprime_usuario` que imprime: "Gabriel (gabriel@exemplo.com)", para uma instância com `nome = "Gabriel"` e `email = "gabriel@exemplo.com"`
    4. Classe `Usuario` deve possuir um *atributo de classe* `quantidade` que armazena a quantidade de instâncias criadas, sejam instâncias de `Usuario` ou de qualquer classe *que estenda `Usuario`.* Por exemplo: `Administrador(Usuario)`.
2. Módulo `administrador.py`
    1. Deve conter uma classe `Administrador` que estende (herda de) `Usuario`.
    2. Deve *sobrescrever* o método `imprime_usuario` e imprimir: "Gabriel (gabriel@exemplo.com) – Administrador", para uma instância com `nome = "Gabriel"` e `email = "gabriel@exemplo.com”`
3. Módulo `main.py`
    1. Deve importar os módulos `usuario.py` e `administrador.py`.
    2. Deve ser executado com as instruções abaixo:
    ```python
    u = Usuario("Gabriel", "gabriel@exemplo.com")
    a = Administrador("Admin", "admin@exemplo.com")
    u.imprime_usuario()
    # => "Gabriel (gabriel@exemplo.com)
    a.imprime_usuario()
    # => "Admin (admin@exemplo.com) – Administrador"
    print(Usuario.quantidade)
    # => 2
    ```
