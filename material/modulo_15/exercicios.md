# Exercícios


## Exercício 1 – Testando a listagem de agendamentos

Escreva um teste para a API de listar agendamentos (`GET /api/agendamentos/`) para o caso de haver um ou mais instâncias de `Agendamento` criadas.


## Exercício 2 – Testando a criação de agendamentos

Escreva casos de teste para a criação de um agendamento. Lembre-se de cobrir pelo menos os dois casos principais: validação bem-sucedida e Agendamento criado; validação mal sucedida e resposta `HTTP 400 Bad Request`.

Para o caso onde a validação é bem-sucedida (*happy path*), faça pelo menos 3 tipos de *assertions*:

1. Verificar a resposta da API (status = 201 e corpo da resposta).
2. Verificar os atributos da instância de `Agendento` em comparação aos valores no corpo da requsição.
3. Após o POST bem-sucedido, fazer um GET em `/api/agendamentos/<pk>/` onde `<pk>` deve ser a chave-primária da instância recém-criada. Verificar que a resposta do GET é o que você espera.

O POST utilizando o `APITestClient` pode ser feito da seguinte maneira:

```python
response = self.client.post(url, data, format='json')
```

Se você não quiser ficar passando o parâmetro `format=json` em todo teste, você pode adicionar o seguinte valor no arquivo `tamarcado/settings.py` (do projeto):

```python
# settings.py
REST_FRAMEWORK = {
    'TEST_REQUEST_DEFAULT_FORMAT': 'json',
}
```


## Exercício 3 – Timezone

Corrija as criações de `Agendamento` no testes para utilizar fuso-horário (`tzinfo`).

Exemplo de como utilizar datetime com e sem timezone:

```python
from datetime import datetime, timezone

data_horario_tz = datetime(2022, 1, 1, 13, 0)
data_horario_sem_tz = datetime(2022, 1, 1, 13, 0, tzinfo=timezone.utc)
print(data_horario_tz == data_horario_sem_tz) # False!!

tz_brasil = timezone(offset=timedelta(hours=-3))  # Cria um fuso-horário em -3 (Brasil)
dt_brasil = datetime(2022, 1, 1, hour=13, tz=tz_brasil)  # Cria um datetime às 13h em Brasil
dt_utc =  datetime(2022, 1, 1, hour=16, tz=timezone.utc)  # Cria um datetime às 16 em UTC (Z)
assert dt_brasil == dt_utc  # True!
```


## Exercício 4 – Function Based Views (FBV) e Class Based Views (CBV)

Após escrever testes para as views de Agendamento (`/api/agendamentos/` e `/api/agendamentos/<id>/`), transforme essas views de FBV => CBV. Seus testes devem continuar passando após essa mudança!


## Exercício 5 – Generic Views

Reescreva as CBV utilizando Generic Views. Escolha a Generic View apropriada: as que já estão implementadas pelo Django Rest Framework podem ser encontradas [na documentação](https://www.django-rest-framework.org/api-guide/generic-views/#concrete-view-classes).

> Se você implementou comportamento customizado para alguma das operações, como por exemplo, definir `agendamento.cancelado = True` para a operação `DELETE` ao invés de deletar a instância, você vai precisar sobrescrever o método `perform_destroy(self, instance)` em `AgendamentoDetail`.

```python
class AgendamentoDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Agendamento.objects.all()
    serializer_class = AgendamentoSerializer

    def perform_destroy(self, instance):
        instance.cancelado = True
        instance.save()
```

Você pode ler mais sobre os métodos de APIs genéricas (`GenericAPIView`) na [documentação](https://www.django-rest-framework.org/api-guide/generic-views/#methods).


## Exercício 6 – Associação entre Usuário (prestador) e Agendamento

Faça a implementação dos seguintes requisitos (apresentado em aula):
- Todo `Agendamento` deve estar associado a um `Usuario` cadastrado.
  - Lembre-se que você vai precisar associar instâncias de `Agendamento` que já tenham sido criadas a algum usuário.
- A partir de uma instância de usuário, deve ser possível buscar os agendamentos associados a este usuário através de um atributo `agendamentos`. Por exemplo: `usuario.agendamentos`.
  - Dica: parâmetro `related_name` no campo `models.ForeignKey`
- Ao solicitar a listagem de agendamentos, o cliente deve fornecer um `username` via `query_params`.
  - Por exemplo: `GET /api/agendamentos/?username=alice`
- Ao solicitar os **horários disponíveis** (implementação do Projeto Final do módulo 14), o cliente também deve passar o `username` do prestador de serviços para visualizar os horários disponíveis desse prestador.
- Para criar um novo `Agendamento`, o cliente deve fornecer o `username` do prestador de serviço como `query_params`.

Exemplo de requisição para criar um `Agendamento`:
```json
POST /api/agendamentos/
Body: 
{
    "data_horario": "2022-03-22T10:00",
    "nome_cliente": "Carl",
    "email_cliente": "carl@codar.me",
    "telefone_cliente": "+5521999978888",
    "prestador": "bob"  // bob deve ser o username de uma instância de User cadastrada no sistema
}
```

> Após criar essa associação, vai ser necessário atualizar os testes, pois antes as instâncias de `Agendamento` não eram associadas a um `User`. Para ver exemplos de como criar uma instância de `User` via código, acesse [a documentação](https://docs.djangoproject.com/pt-br/4.0/topics/auth/default/#creating-users)

> Também será necessário atualizar a funcionalidade de listar horários disponíveis, pois agora ela deve considerar que cada prestador tem sua própria agenda, ou seja, se houver um Agendamento às 9h00 para a prestadora "Alice", o horário de 9h00 continua disponível na agenda do prestador "Bob".


## Exercício 7 – Autenticação e Autorização

Adicione permissões às views de modo que as seguintes regras sejam respeitadas:
- Qualquer cliente, autenticado ou não, deve ser capaz de criar um `Agendamento` associado a um prestador.
- Qualquer cliente, autenticado ou não, deve ser capaz de visualizar os **horários disponíveis** de um determinado prestador.
- Apenas o prestador associado a um determinado `Agendamento` pode:
  - Visualizar detalhes do agendamento;
  - Editar o agendamento;
  - Cancelar (`DELETE`) o agendamento;
- Apenas um usuário autenticado pode ver a listagem de agendamentos dele. Usuários, autenticados ou não, não podem acessar a listagem de agendamentos de outros usuários.


## Exercício 8 – Testes para Permissões

Atualize os testes que estiverem falhando e adicione novos casos de testes para as permissões utilizadas. Exemplos:
- Usuária "alice" não deve ter acesso a listagem de agendamentos do usuário "bob";
- Usuário "alice" deve conseguir visualizar agendamentos associados à ela – tanto listagem quanto individualmente.

Você provavelmente vai precisar criar instâncias da classe `User` (importada de `django.contrib.auth.models.User) e **autenticar** essas instâncias para conseguir fazer a requsição.

A maneira mais simples de autenticar um usuário nos testes é utilizando o método `client.force_authenticate(request, user)`:
```python
from rest_framework.test import APIClient

client = APIClient()
client.force_authenticate(user)
cliente.get(...)
```

Ou, dentro de uma classe que herda de APITestCase:
```python
class TestListagemAgendamentos(APITestCase):
    def test_listagem(self):
        user = User.objects.create(email="bob@email.com", username="bob", password="123")
        self.client.force_authenticate(user)
        self.client.get("/api/agendamentos/?username=bob")
```

E outra opção é você realizar o `login`:
```python
class TestListagemAgendamentos(APITestCase):
    def test_listagem(self):
        user = User.objects.create(email="bob@email.com", username="bob", password="123")
        self.client.login(username="bob", password="123")
        self.client.get("/api/agendamentos/?username=bob")
```


## Exercício 9 – Listagem de prestadores e agendamentos

Faça a implementação de uma view que liste todos os prestadores de serviço cadastrados e seus respectivos agendamentos.

Os agendamentos devem ser serializados da mesma maneira que na listagem de agendamentos (ou seja, não é para exibir apenas o *id*, mas sim a representação do objeto como JSON).

Essa view deve ser acessada **somente por administradores** (superuser).

> Dica: dê uma olhada nas [permissões do Django Rest Framework](https://www.django-rest-framework.org/api-guide/permissions/#isadminuser)


# Projeto Final

Aqui listamos algumas sugestões de funcionalidades que poderíamos adicionar ao nosso projeto. Provavelmente você vai precisar pesquisar na documentação do Django Rest Framework para implementar algumas delas e é altamente recomendado que pessa ajuda na nossa comunidade do Discord!


## Confirmação de agendamento

Qualquer pessoa pode criar um novo `Agendamento` com determinado prestador de serviço. Por isso, é importante que o próprio prestador possa *confirmar* ou não um determinado agendamento.

Implemente a funcionalidade de *confirmação de agendamento*:
- Todo `Agendamento` recém-criado deve ser considerado como **não confirmado**.
- Apenas o prestador de serviço pode **confirmar um agendamento**. Isso pode ser implementado de pelo menos duas maneiras:
  - Através do `PUT/PATCH` na API de detalhes do Agendamento.
  - Através de uma nova API (rota), por exemplo: `POST /api/agendamentos/<pk>/confirmar/`
- Ao fazer a listagem de agendamentos, o cliente pode passar um outro `query_param` indicando se gostaria de visualizar apenas agendamentos confirmados, ou apenas agendamentos não-confirmados.
  - `GET /api/agendamentos/?username=alice&confirmado=true`
    - Retorna apenas agendamentos **confirmados** associados à `alice`.
  - `GET /api/agendamentos?username=alice&confirmado=false`
    - Retorna apenas agendamentos **não confirmados**.
  - `GET /api/agendamentos?username=alice`
    - Retorna todos agendamentos de `alice`, confirmados ou não.

> Observe que podemos passar múltiplos parâmetros de query (*query params*) utilizando o separado `&` entre cada um deles: `?a=1&b=2&c=3`


## Agendamentos confirmados e horários disponíveis

No módulo 14 implementamos a listagem de horários disponíveis. Agora vamos incrementar essa funcionalidade da seguinte maneira:

- Um novo `Agendamento` só pode ser criado se o horário solicitado está **disponível**.
- Um `Agendamento` só torna determinado horário **indisponível** quando é **confirmado**.
- Um `Agendamento` só pode ser **confirmado** se o horário ainda estiver disponível.
  - Ou seja, posso ter 2 agendamentos **não confirmados** no mesmo horário, porém só um deles vai poder ser **confirmado**.


## Estados de um Agendamento

Implemente a habilidade de saber se um determinado `Agendamento` foi realmente **executado** ou não.

* Podemos pensar em adicionar um atributo *booleano* "executado" no nosso modelo de `Agendamento`. Mas será que é a melhor opção?
  * O problema dessa abordagem é que acabamos tendo que lidar com muitos valores "conflitantes". Por exemplo: um agendamento não pode estar "confirmado" e "cancelado" ao mesmo tempo. Assim como não pode estar "cancelado" e "executado".
* Uma outra possibilidade é agrupar esses possíveis **estados** de um Agendamento (não-confirmado, confirmado, executado, cancelado...) em um único campo. [Considere utilizar algo como o `Field.choices` do Django](https://docs.djangoproject.com/en/4.0/ref/models/fields/#choices)


## Programa de fidelidade

Ao **executar** um Agendamento, caso o e-mail do cliente pertença a um usuário cadastrado na plataforma, devemos adicionar um ponto de fidelidade a esse usuário.

* Note que os pontos devem ser para cada usuário e prestador de serviço!
  * Ou seja, um usuário pode ter 10 pontos de fidelidade com o Prestador A e apenas 5 com o Prestador B.
* Para implementar isso temos algums opções:
  * Podemos ter um novo **modelo** (tabela) `Fidelidade` que associa um certo usuário a um prestador (que também é um usuário) a uma certa quantidade de pontos.
  * Observe que, nesse caso, a tabela `Fidelidade` deve ter uma restrição de *unicidade* para a chave composta por `(cliente, prestador)`.


# Modelagem de Banco de Dados

O foco dessa seção é fazer você pensar em como adaptar os nossos modelos e/ou criar uma nova modelagem para acomodar novos requisitos que surgem.

Não tem uma resposta certa/errada para a modelagem.

Não é necessário implementar as APIs para esses requisitos, apenas a camada de *modelos*. Se preferir, pode criar um projeto separado para evitar misturar as coisas.

* Como poderíamos ter estabelecimentos que oferecem diferentes serviços?
  * Por exemplo, o mesmo salão de beleza pode oferecer serviços como "corte de cabelo" e "pedicure".
  * Esse mesmo salão poderia ter diferentes valores para diferentes serviços.
* Diferentes funcionários de um certo estabelecimento poderiam prestar diferentes tipos de serviço
  * Ou seja, o mesmo salão pode ter 2 agendamentos para o mesmo horário, desde que não seja com o mesmo profissional.
  * Cada profissional deve ter um conjunto de serviços que ele é capaz de prestar.

Possivelmente você vai precisar de novos modelos e de diferentes associações. Por exemplo: um Agendamento agora está associado a um prestador, a um estabelecimento, ou aos dois? A lista de serviços disponíveis pode ser expressa como uma tabela? Como eu associo um serviço a um determinado profissional, indicando que ele é capaz de prestar aquele serviço?

Essas são só algumas das perguntas que sua modelagem deve ser capaz de responder.
