# Resumo módulo 12

## Componentes

Nesse módulo apredemos a utilizar a framework Django. Ela é considerada uma framework fullstack, alguns do principais componentes são:
- `urls.py`: onde mapeamos uma *rota* para uma função (*view*)
- `views.py`: funções que são chamadas quando determinada *url* é acessada. Elas recebem pelo menos um objeto `request` (tipo: `HttpRequest`) como parâmetro e devem retornar um `HttpResponse`.
- `templates`: arquivos HTML com funcionalidades especiais (graças ao Django Tempalte). Por exemplo: renderizar diversos elementos HTML de acordo com uma lista de objetos.
- `models.py`: onde ficam os *modelos* da nossa aplicação (ou *entidades*). Quando heram de `django.db.models.Model`, são mapeadas para tabelas e atributos em um banco de dados.
- `shell`: um modo de interagir com nossa aplicação via shell. Geralmente utilizada para rascunhos, escrever consultas e testar coisas, mas nada impede que seja utilizada de outras formas.
- `admin`: painel de administração onde podemos interagir com os nossos modelos.
- `migrations`: todas as alterações nos nossos modelos que devem refletir mudanças em um banco de dados são feitas em duas etapas. Primeiro, é gerado o arquivo de migração que representa o que vai ser alterado. Segundo, esse arquivo é executado e as mudanças são realizadas no banco de dados.

## Principais comandos utilizados

```bash
django-admin startproject <nome-projeto>
django-admin startapp <nome-app>
python manage.py runserver
python manage.py makemigrations
python manage.py migrate
python manage.py shell
python manage.py dbshell
```


## Principais objetos e métodos utilizados

```python
django.http.HttpResponse
django.http.HttpRequest
django.http.HttpResponseRedirect
django.shortcuts.render
django.shortcuts.get_object_or_404
django.urls.reverse
django.urls.path
django.db.models.Model.objects.create(...)
django.db.models.Model.objects.filter(...)
django.db.models.Model.objects.get(...)
evento.save()  # evento = Evento(...)
```

## Principais comandos em um template HTML
```django
{% for elemento in lista %} ... {% endfor %}
```
```django
{% if <condição> %}
    ...
{% elif <condição> %}
    ...
{% else %}
    ...
{% endif %}
```


# Referências

- [Exercícios](exercicios.md)
- [Requisitos do projeto](TODO.md)
- [Slides da aula de banco de dados](Módulo%2012,%20Banco%20de%20dados.pdf)
- [Extensão Django VSCode](https://marketplace.visualstudio.com/items?itemName=batisteo.vscode-django)
- [SQLZoo: Tutorial de SQL Prático (inglês)](https://sqlzoo.net/wiki/SQL_Tutorial)
- [Documentação oficial Django](https://docs.djangoproject.com/pt-br/4.0/)
- [Documentação Django sobre CSRF](https://docs.djangoproject.com/pt-br/4.0/ref/csrf/)
- [Vídeo sobre CSRF](https://www.youtube.com/watch?v=vRBihr41JTo)