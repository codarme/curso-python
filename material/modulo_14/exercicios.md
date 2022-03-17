# Exercícios


### Exercício 1 – Git e GitHub

Crie um repositório no GitHub e faça "push" do seu projeto Django com os arquivos iniciais do projeto "tamarcado". Lembre-se de adicionar arquivos desnecessários ao `.gitignore` (`.sqlite3`, `venv`, `__pycache__`, ...).


### Exercício 2 – Shell e Django Admin

Crie instâncias de `Agendamento` pelo `shell` e/ou pelo `Django Admin`.
* Lembre-se que é necessário registrar o modelo no arquivo `admin.py`: `admin.site.register(<modelo>)`.
* Você provavelmente vai precisar criar um `superuser` para conseguir acessar o `Django Admin`.
  * `python manage.py createsuperuser`
* Você vai precisar utilizar o módulo `datetime` do Python para fornecer valores para o atributo `data_horario`.


### Exercício 3 – Postman

Configure uma nova coleção de requisições no Postman de acordo com as especificações da [nossa API](./design-api.md).


### Exercício 4 – Implementação: Criar, listar, detalhar

Implemente a criação, listagem e detalhamento de `Agendamentos`. Se você preferir, pode utilizar o arquivo [views.py](./views.py) como base.


### Exercício 5 – Cancelar vs Excluir

Ao invés de excluir uma instância de Agendamento, altere o valor do atributo `cancelado` para `True`. Eventos cancelados **não devem ser listados**.

P.S.: Se você quiser que alguém avalie sua implementação desse exercício, **abra um pull request** a partir de uma nova branch para a branch principal do seu projeto com a implementação do exercício e envie o link na nossa comunidade do Discord, marcando algum instrutor.


### Exercício 6 – Validações

Implemente as validações abaixo:

1. Incremente a validação feita para o atributo `telefone_cliente`, seguindo a especificação:
   1. Deve conter no mínimo 8 dígitos;
   2. Deve ser composto apenas de dígitos (0 - 9), com exceção de caracteres especiais como *parêntesis* `(` e `)`, hífen `-`, e sinal de mais `+`. Este último, se presente, deve estar na primeira posição da string.
2. O mesmo usuário (identificado por `email_cliente`) **não** pode realizar **mais de um agendamento** no mesmo **dia**.
   1. P.S.: Você pode utilizar o método `dt.date()` (onde `dt` é um objeto do tipo `datetime`) para obter a **data** (apenas o dia).
3. **DESAFIO**. O horário de um agenddamento deve ter um espaço de **30 minutos** entre outros agendamentos. Ou seja, caso exista um agendamento às `2022-03-01T12:30`, outros agendamentos só podem ser criados nas seguintes condições:
   1. `data_horario <= 2022-03-01T12:00`; ou
   2. `data_horario >= 2022-03-01T13:00`;


### Projeto Final – Listando horários disponíveis

Crie uma nova API `GET /horarios/?data=YYYY-MM-DD` que retorna a lista de horários disponíveis para um determinado dia (data) de uma loja que presta um único tipo de serviço.

#### Regras de Negócio

* A loja abre às 09h00 e fecha às 18h00. Ou seja, o primeiro horário disponível é de 09h00 às 9h30 e o último de 17h30 às 18h00.
* O horário de almoço é de 12h00 às 13h00, entre esses horários não deve haver a prestação de serviços.
* Quando agendamentos são realizados para um determinado horário em uma certa data, aquele horário não deve mais estar disponível.
* Agendamentos podem ser cancelados, o que faz com que o horário do agendamento se torne novamente disponível.
* (DESAFIO) Aos Sábados, a loja abre às 09h00 e fecha às 13h00 e não tem horário de almoço.


#### Detalhes de implementação

**Query Params e Conversão para Date**

URLs podem conter o que chamamos de `query params` ou `parâmetros da consulta`. Esses parâmetros são adicionados ao fim da URL e separados da URL por um `?`.

Podemos utilizar o atributo [`request.query_params`](https://www.django-rest-framework.org/api-guide/requests/#query_params) para obter um dicionário com `query params` da URL. Os valores dos parâmetros vêm como `string`, então precisamos converter para o tipo desejado.

```python
from datetime import datetime
# GET /horarios/?data=2022-03-20
@api_view(http_methods_list=["GET"])
def listar_horarios(request):
    data = request.query_params.get("data")  # query_params = {"data": "2022-03-20"}
    # data = "2022-03-20", precisamos converter para um tipo `date`
    data = datetime.fromisoformat(data).date()
    ...
```

---

**Filtrando date de campo DateTimeField**

Podemos utilizar o filter da seguinte maneira para comparar um `DateTimeField` com um objeto do tipo `date`:
```python
# Buscar agendamentos com data_horario cujo dia seja igual a 20 de Março de 2022
Agendamento.objects.filter(data_horario__date=date(2022, 3, 20))
```

---

**Atenção aos fuso-horários**

Objetos `datetime` podem ter um fuso-horário especificado através do parâmetro opcional `tzinfo`
```python
from datetime import datetime, timezone

dt_com_timezone = datetime(2022, 3, 20, tzinfo=timezone.utc)
dt_sem_timezone = datetime(2022, 3, 20)


assert dt_com_timezone == dt_sem_timezone  # Vai falhar! São considerados diferentes
```

---

**Dia da semana**

Para saber o **dia da semana** de uma data, podemos utilizar o método `date.weekday()`, que retorna um **inteiro** representando o dia da semana, segundo a tabela abaixo:

| weekday() | dia da semana |
|-----------|---------------|
| 0         | Segunda-feira |
| 1         | Terça-feira   |
| 2         | Quarta-feira  |
| 3         | Quinta-feira  |
| 4         | Sexta-feira   |
| 5         | Sábado        |
| 6         | Domingo       |

---

**Uma ajudinha**

[Esse gist](https://gist.github.com/gcrsaldanha/6841e0ddabe863688b8d0e4b56239deb) tem um breve exemplo sobre como utilizar `datetime` e `timedelta` para gerar um novo `datetime`.
