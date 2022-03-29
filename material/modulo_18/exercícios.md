# Exercícios Módulo 18


## Exercício 1 – Gerando arquivo em CSV

Implemente uma API cuja resposta seja um arquivo CSV para Download. O arquivo CSV deve ter como primeira linha as colunas da "tabela" (*headers*).

Referências:
- [Python CSV](https://docs.python.org/3/library/csv.html)
- [Django Output as CSV](https://docs.djangoproject.com/en/4.0/howto/outputting-csv/#using-the-python-csv-library)


## Exercício 2 – Refatorando

Extraia a escrita de CSV para um módulo separado, por exemplo, `utils.py`.


## Exercício 3 –  Salvando valores no Redis

Siga as [instruções oficiais para instalar o Redis no seu computador](https://redis.io/docs/getting-started/installation/) e iniciar o servidor *redis*. Após isso, execute os seguintes comandos no terminal:
```bash
redis-cli
127.0.0.1:6379> ping
PONG
127.0.0.1:6379> SET teste 10
OK
127.0.0.1:6379> GET teste
"10"
127.0.0.1:6379>
```


## Exercício 4 – Executando uma tarefa assíncrona

1. Crie um arquivo `celery.py`
```python
from celery import Celery
app = Celery(
  'tamarcado',  # Nome do app celery
  broker='redis://localhost:6379/0',  # Message broker
  backend='redis://localhost:6379/0',  # Salvar resultados das tasks
)

@app.task
def add(x, y):
    return x + y
```

2. Execute o celery worker
```bash
celery -A tamarcado worker -Q celery --loglevel=INFO
```

3. Abra uma sessão do `python` e execute a função `add`
   1. Primeiro chamando `add(1, 2)`
   2. Depois, invocando com `add.delay(1, 2)`

4. Execute o `redis-cli` e verifique que as mensagens foram inseridas (`KEYS *` para ver todos os valores armazenados no banco).


## Exercício 5 – Relatório assíncrono

Refatore a view de gerar o relatório de forma que ela execute a geração de relatório de maneira assíncrona (em uma *task*).

* Cuidado para não fazer *queries* desnecessárias na *view*.
  * por exemplo, se a consulta vai acontecer na task, não é preciso fazê-la antes de chamar a task.
* Utilize `StringIO` como um objeto *gravável* para escrever os valores em CSV.
  * Você pode utilizar o método `StringIO.getvalue()` para verificar que a escrita foi realizada corretamente.

> Para sua *task* ser "descoberta" é necessário utilizar a função `autodiscover_tasks()` e definir qual é o arquivo de configuração do Django utilizado.

```python
# celery.py
...
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'tamarcado.settings.dev')
...
app.autodiscover_tasks()
```


## Exercício 6 - Enviando e-mails

Envie um e-mail com anexo e visualize o mesmo através do MailHog.

1. [Instale e execute o MailHog](https://github.com/mailhog/MailHog/releases/v1.0.0).
2. Configure as variáveis de email do Django.
```python
EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
EMAIL_HOST =  '0.0.0.0'
EMAIL_PORT =  1025
```
3. Envie um e-mail com anexo. Utilize a classe [EmailMessage](https://docs.djangoproject.com/en/4.0/topics/email/#emailmessage-objects).


## Exercício 7 – Logging

Adicione `logs` ao longo da nossa tarefa para facilitar visualizar o fluxo do que está acontecendo.


## Exercício 8 – E-mail do destinatário

Altere o e-mail do destinatário para ser o e-mail do usuário que fez a requisição.


## Exercício 9 – Configurando SMTP em produção

Crie sua conta no [SendGrid](https://signup.sendgrid.com/) e siga [o passo-a-passo para realizar a integração SMTP](https://app.sendgrid.com/guide/integrate/langs/smtp) com seu projeto Django.

Você deve conseguir os valores para as seguintes variáveis:
```python
EMAIL_HOST = 'smtp.sendgrid.net'
EMAIL_PORT = 587
EMAIL_HOST_USER = 'apikey'
# CUIDADO PARA NÃO FAZER COMMIT DA SUA API_KEY!!!
# ELA DEVE ESTAR EM UM ARQUIVO .env NÃO VERSIONADO!
EMAIL_HOST_PASSWORD = os.environ.get('SENDGRID_API_KEY')
```

Execute seu projeto com as configurações de produção e verifique que você recebe o e-mail na caixa do destinatário.

> Você deve alterar o "from" no objeto `EmailMessage` para o e-mail que você informou no SendGrid.
> Verifique os logs da aplicação, caso nenhum erro ocorra, verifique a **caixa de SPAM** do destinatário.


## Exercício 10 – Utilizando variáveis de configuração para o Celery

Altere a inicialização do app `celery` para ler configurações do message broker e backend result a partir de variáveis de configuração.


```python
# celery.py
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'tamarcado.settings.dev')
app = Celery('tamarcado')
app.config_from_object('django.conf:settings', namespace='CELERY')
```

> É necessário adicionar `CELERY_BROKER_URL` e `CELERY_RESULT_BACKEND` ao seu arquivo de configuração (`settings`).


## Exercício 11 – Configurando remetente

Altere o "from" no objeto `EmailMessage` para ser um valor que é obtido a partir das `settings`, e, por sua vez, a partir do arquivo *dotenv*.


## Exercício 12 – Refatorando e testando

Escreva testes para a sua task de gerar e enviar relatório por e-mail. Pode ser mais fácil dividi-la em duas ou mais funções e testá-las individualmente.

[Na documentação do Django](https://docs.djangoproject.com/pt-br/4.0/topics/testing/tools/#email-services) tem um exemplo sobre como verificar a caixa de saída do servidor SMTP de teste.

> Você pode escrever testes invocando a celery task como uma função qualquer caso queira que ela seja executada de maneira assíncrona.


## Exercício 13 –  Deploy no Heroku

Passo-a-passo para realizar o deploy da aplicação no Heroku.

1. Atualizar o seu arquivo `requirements.txt`
```text
celery[redis]==5.2.3
```
> Você pode utilizar `pip freeze` para ver a versão do Celery instalada.

2. Atualizar o `Procfile` com o comando `worker`
```Procfile
release: python manage.py migrate
worker: celery -A tamarcado worker -Q celery --loglevel=info
web: gunicorn tamarcado.wsgi
```

3. Provisionar o Redis para a sua aplicação heroku
```bash
heroku addons:create heroku-redis --remote <nome do git remote>
# Ou
heroku addons:create heroku-redis --app <nome do app heroku>
```

> Se você ainda não o fez, crie duas variáveis de configuração: `CELERY_BROKER_URL` e `CELERY_RESULT_BACKEND` que leem de uma variável de ambiente chamada `REDIS_URL`

4. Configurar os valores do servidor SMTP em produção
   1. EMAIL_HOST
   2. EMAIL_PORT
   3. EMAIL_HOST_USER
   4. EMAIL_HOST_PASSWORD
   5. EMAIL_FROM

> Você também pode alterar esses valores através do [Dashboard](https://dashboard.heroku.com).

5. Fazer um *push* para o seu app heroku e esperar o deploy.

> Para visualizar os logs: `heroku logs --remote <git remote> --tail`

A partir de agora, você deve ser capaz de enviar e-mail a partir de sua aplicação em produção!