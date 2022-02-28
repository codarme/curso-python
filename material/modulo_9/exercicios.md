# Exercícios HTTPServer

Tendo como base o arquivo [base_server.py](base_server.py) e o template HTML [listar_usuarios.html](listar_usuarios.html), implemente um servidor utilizando a classe `HTTPServer` do Python nas seguintes especificações:
* O servidor deve possuir uma lista de `Usuários`
* Toda instância de `Usuário` deve possuir os atributos:
  * id (int)
  * nome (str)
  * email (str)
  * senha (str)
* O atributo `id` deve ser auto-incrementado para cada novo usuário criado.
* O servidor deve possuir uma rota `/usuarios/` que lista os usuários criados em uma tabela, de acordo com o template [listar_usuarios.html](listar_usuarios.html)
  * A coluna "Senha" deve exibir o valor dos 5 primeiros caracteres do *hash* da senha do usuário, seguidos de reticências ("..."), e não a senha em si.
    * Ex.: Senha: "123", `hash_string("123") -> "a665a45920422f9d417e4867efdc4fb8a04a1f3fff1fa07e998e86f7f7a27ae3"`
    * Deve exibir apenas: `a665a...`


## Dicas
* Em Python existe o operador "slice", que retorna um pedaço de uma lista ou string.
```python
>>> nome = "Francine"
>>> print(nome[0:5])  # elemento 0 (inclusivo) até o elemento na posição 4 (5 menos 1, pois é exclusivo)
Franc
```
* Lembre-se de definir o cabeçalho `Content-Type` para garantir que acentos funcionem corretamente.
  * Valor: `"text/html; charset=utf-8"`
* Utilizamos o `status_code = 200` para indicar uma operação bem sucedida.
* A função `hash_string` já está implementada no arquivo [base_server.py](base_server.py) para você utilizar.
* O método `self.wfile.write` recebe dados do tipo `binário`. Para codificar uma `string` em binário, podemos utilizar o método `str.encode()`.