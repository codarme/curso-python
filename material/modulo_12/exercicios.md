# Exercícios – Django

1. Implemente uma aplicação seguindo os requisitos no arquivo [TODO.md](TODO.md) e baseando-se nos templates disponíveis em [design/](design/).
2. Crie uma nova página para visualizar os detalhes de uma Categoria a partir de seu id. Ex.: `/categorias/<int:id>`.
3. Crie uma nova página para visualizar todas as categorias criadas. Ex.: `/categorias/`.
4. Nem sempre a nossas *regras de negócio* são as mesmas regras seguidas pelo banco de dados. Por exemplo: o nosso banco permite que as colunas `local` e `link` sejam preenchidas para um mesmo Evento. Porém, nosso cliente informou que um Evento deve possuir **ou um local**, **ou um link**, e não os dois simultaneamente.
    1. Crie um *`classmethod`* responsável por criar um Evento (`Evento.cria_evento(...)` ) que faça essa validação e caso esteja tudo OK, crie o evento no banco de dados.
    2. Lance uma exceção caso os dois valores sejam passados. Para lançar uma exceção no Python, você pode utilizar a palavra especial `raise`. Exemplo: `raise ValueError("Evento não pode possuir local e link.")`
    ```python
   class Evento(models.Model):
       ...

       @classmethod
       def cria_evento(cls, nome, local, link, ...):
           # TODO: implementar esse método
           evento = Evento(...atributos)
           return evento
   ```
    1. Crie um evento através do `shell` (`manage.py shell`) utilizando o método `cria_evento` e tente criar um evento com *local e link*.
5. O argumento `blank=False` passado para um atributo `models.CharField` não é verificado quando criamos objetos utilizando o ORM (`Categoria.objects.create(...)` ou `Categoria(...).save()`).
   1. Crie um `classmethod` em `Categoria` que receba um `nome` e lance uma exceção caso `nome` seja vazio ou nulo. Caso contrário, o método deve criar uma nova instância de `Categoria`, persistir no banco de dados e retornar essa instância.
   ```python
   class Categoria(models.Model):
       nome = models.CharField(max_length=256, blank=False, unique=True)

       @classmethod
       def cria_categoria(cls, nome):
           # TODO: implementar esse método
           categoria = ...
           return categoria
   ```
6. **DESAFIO.** Podemos utilizar o método [`order_by(campo)`](https://lucid.app/lucidchart/02718f5c-abb2-4daa-a466-9303072cb322/edit?invitationId=inv_f8eb107e-064b-440b-806b-d26870833b59) onde `campo` é uma string com o nome de um dos campos do nosso modelo para ordenar os resultados de uma consulta de maneira crescente. Também podemos usar `order_by(-campo)` para ordenar de maneira decrescente. Altere a consulta para listar eventos de modo que eles sejam exibidos do mais próximo para o mais distante (lembrando que eventos que já passaram não devem ser listados).
7. **DESAFIO.** Na página de detalhes de uma categoria, adicionar um novo parágrafo informando a **quantidade de eventos** com essa categoria.
    Dica:
    ```python
    eventos = Evento.objects.all()
    qtd_eventos = eventos.count()  # .count() retorna a quantidade de registros em um QuerySet
    ```
