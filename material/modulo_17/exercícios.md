# Exercícios Módulo 17


## Exercício 1 – Criando uma nova conta no Heroku

Crie uma nova conta no [Heroku](https://signup.heroku.com/) e instale o [Heroku CLI](https://devcenter.heroku.com/articles/heroku-cli).


## Exercício 2 – Deploy do nosso projeto para o Heroku

1. Copie os arquivos de configuração na pasta [config_heroku/](config_heroku/) para o seu projeto.
   1. Talvez seja necessário fazer alguns ajustes de acordo com as configurações do seu projeto atual.
2. Crie um novo app do heroku (`heroku create`).
3. Adicione as variáveis de configuração ao seu aplicativo heroku criado (`heroku config:set CHAVE=VALOR`):
   1. `SECRET_KEY`
   2. `DJANGO_SETTINGS_MODULE`
4. Faça um push a partir de sua branch `main` para o remote do heroku: `git push heroku main`
5. Acesse a sua aplicação em produção!

> Caso necessário, você pode visualizar sua aplicação em https://dashboard.heroku.com.


## Exercício 3 – Criando e visualizando agendamentos

Crie agendamentos via django admin (em produção!) e faça uma requisição para visualizá-lo via Chrome ou Postman.

* Caso ainda não o tenh feito, adicione `rest_framework` à lista `INSTALLED_APPS` (settings).
  * Isso adiciona os templates da biblioteca Rest Framework ao nosso projeto.
* Adicione `path('api-auth/', include('rest_framework.urls'))` às urls do **projeto**.
  * Isso adiciona as views que permitem você autenticar através do navegador para acessar a *Browsable API* do Rest Framework.


## Exercício 4 – Configurando o Postman

* Crie diferentes ambientes para representar produção e desenvolvimento.
* Adicione variáveis como *host* e *username* com seus respectivos valores em cada ambiente.

> Durante a aula nós salvamos o password como uma variável no Postman, mas isso **não** é uma boa prática, pois é comum compartilharmos ambientes do Postman e nesse caso poderíamos acabar compartilhando informações de login.

Se quiser adicionar uma variável para *password* também, recomendo a leitura sobre [Secret Variables](https://blog.postman.com/introducing-secret-variable-type-in-postman/) do Postman.


## Exercício 5 – Criar um novo usuário

Crie um novo *endpoint* para a criação de usuários. Uma sugestão de contrato para a sua API:

```
POST /api/users/

{
    "username": "admin",
    "password": "1234",
    "email": "admin@email.com"
}
```

> Lembre-se de utilizar o método [`User.objects.create_user`](https://docs.djangoproject.com/en/4.0/ref/contrib/auth/#django.contrib.auth.models.UserManager.create_user).

**Abra um pull request** com a sua modificação e com testes e envie na nossa comunidade para ser avaliado! :)


## Exercício 6 – Gerando backups

Crie um backup agendado (*scheduled backup*) para ser realizado todos os dias às 2 horas da manhã **no horário de Brasília**.

[Documentação para realizar backups](https://devcenter.heroku.com/articles/heroku-postgres-backups).


##  Exercício 7 - Criando um novo ambiente

- Crie um novo app de homologação e configure-o com as devidas variáveis.
- Renomeie seus *git remotes* para *production* e *staging*.
- Faça deploy em ambos ambientes:
  - `main` => `production`
  - `develop` => `staging`

[Documentação sobre múltiplos ambientes no Heroku](https://devcenter.heroku.com/articles/multiple-environments).


## Exercício 8 – Copiando dados de produção para homologação

Copie os dados do seu banco de produção para o seu banco de homologação.

[Documentação para restaurar backups](https://devcenter.heroku.com/articles/heroku-postgres-backups#restoring-backups).


## Exercício 9 – Deploy Contínuo

Configure seu projeto para realizar deploys automaticamente nos ambientes de *staging* e *production*:
- Merge em *develop* => dispara deploy em *staging*
- Merge em *main* => dispara deploy em *production*

> Lembre-se de acessar o [Heroku Dashboard](https://dashboard.heroku.com/) para habilitar deploys automáticos em cada um de seus apps.


## Exercício 10 – Configurando GitHub Actions

Crie um repositório para o seu projeto (caso não exista) e adicione o arquivo [django.yml](./django.yml) em uma pasta `.github/workflows/`.

> Ou você pode criar o arquivo do GitHub Actions através do próprio site do GitHub, conforme vimos em aula.

Faça os ajustes necessários e abra um Pull Request de `develop` para `main` que execute os seus testes com sucesso. Não faça o merge desse Pull Request antes de ter pelo menos **1 review approval**.


## Exercício 11 – Restrições de branches

Restrinja sua branch `main` de modo que ela só possa receber mudanças através de Pull Requests.

Dica: se você acessar o Dashboard Heroku do seu app, na seção de Deploy, você vai encontrar uma opção **Wait for CI to pass before deploy**. Marque essa opção para prevenir que o Heroku faça um deploy caso os testes (CI) não estejam passando.


## Exercício 12 – Status badge

Adicione uma status badge ao seu projeto!

> Você pode fazer isso acessando um determinado `build` na seção de `Actions` do seu repositório, e selecionando "Create status badge". Adicione esse valor ao seu arquivo `README.md` na raíz do seu repositório.


## Exercício 13 – Renomeando apps

Os nomes de nossos apps podem ser confusos e chatos de se memorizar. [Renomeie seus apps](https://devcenter.heroku.com/articles/renaming-apps) para algum nome específico (por exemplo, nome do projeto).

> Se quiser, pode adicionar "prod" ou "stg" como prefixos. Ex.: "prod-tamarcado" e "stg-tamarcado".
