# Exercícios Módulo 16

## Exercício 1 – Corrigindo `get_horarios_disponiveis`

Caso ainda não o tenha feito, implemente uma função `get_horarios_disponiveis(data, prestador)`, onde `data` é um objeto do tipo `date` e `prestador` é uma instância de `Prestador`.

Essa função deve retornar os horários disponíveis para uma certa data levando em conta os `Agendamentos` daquele `prestador` específico.

> Note que implementamos essa função anteriormente quando não tínhamos a relação `Agendamento –– Prestador`, então considerávamos todos `Agendamentos` como sendo de um único prestador.


[Referência: Exercício de Associação entre Prestador e Agendamento](https://github.com/CodarMe/curso-python/blob/main/material/modulo_15/exercicios.md#exerc%C3%ADcio-6--associa%C3%A7%C3%A3o-entre-usu%C3%A1rio-prestador-e-agendamento)


## Exercício 2 – Exibindo mais informações para o cliente da nossa API

Implemente as seguintes funcionalidades em nossa API:

1. Quando um cliente solicitar os horários disponíveis para uma determinada data, caso essa data seja um feriado nacional, nenhum horário deve estar disponível.
2. Quando um cliente tentar realizar um Agendamento em uma determinada data, caso essa data seja um feriado nacional, o cliente deve receber uma mensagem de erro **específica**, ou seja, diferente de quando não há horários disponíveis porque já existe outro Agendamento.
   1. A intenção desse requisito é evitar que o cliente fique tentando agendar em outros horários naquele mesmo dia.
   2. Observe que a mensagem para quando um horário não está disponível por outros motivos (já existe Agendamento ou o horário solicitado fora do horário de trabalho) deve permanecer como antes.


## Exercício 3 – *Mockando* `get_horarios_disponiveis` na `view`

> Primeiro, garanta que a função que retorna os horários disponíveis para uma certa data e prestador está separada da sua `view` de listar horários disponíveis (pois essa função deve ser utilizada pelo `AgendamentoSerializer` também).

1. Escreva testes unitários para a `view` de listagem de horários disponíveis de modo que a função `get_horarios_disponiveis` **seja Mockada**. Ou seja, devemos ter pelo menos dois testes para a `view`:
   1. `get_horarios_disponiveis` retornando uma lista vazia;
   2. `get_horarios_disponiveis` retornando uma lista com pelo menos um horário disponível.

> A ideia desse exercício é você perceber que podemos testar unidades do nosso código de maneira isolada.


## Exercício 4 – Testes unitários para `get_horarios_disponiveis`

Escreva testes unitários para método `get_horarios_disponiveis`. Utilize a técnica `mock.patch` para *mockar* possíveis respostas de `is_feriado`.


## Exercício 5 – Configurando `pytest` e `coverage`

1. Instale as bibliotecas `pytest-django` e `pytest-cov`
2. Crie um arquivo `pytest.ini` na raíz do projeto com o seguinte conteúdo

```ini
[pytest]
DJANGO_SETTINGS_MODULE = tamarcado.settings  ; Referência ao arquivo "settings.py" do projeto Django
python_files = tests.py test_*.py  ; Arquivos que devem ser considerados arquivos de teste ("Test Discovery")
addopts = --cov=.
          --cov-report term-missing:skip-covered  ; Não exibe arquivos com 100% de cobertura de testes
          --cov-fail-under 100  ; Abaixo de 100% de cobertura de testes é considerado falha
```

3. Execute o comando `pytest` e verifique que seus testes são executados como esperado.
    1. Além de exibir os resultados dos testes, deve ser exibido um relatório sobre a cobertura de testes.
    2. Um arquivo `.coverage` pode ter sido criado na raíz do projeto, adicione `.coverage` ao `.gitignore`
4. Substitua todas as *assertions* (e.g.: `self.assertEqual, self.assertDictEquals`) por simples `asserts`.
5. Caso você queira que alguns arquivos sejam omitidos das métricas de cobertura, por exemplo, `manage.py`, arquivos de migração, ou arquivos que não são nossos (auto-gerados pelo Django):
    1. Crie na raíz do projeto um arquivo chamado `.coveragerc`
    2. Adicione o seguinte conteúdo à ele
```ini
[run]
omit = 
    */migrations/*  ; omite todos arquivos que estiverem em pastas migrations/
    tamarcado/*  ; omite arquivos na pasta do projeto Django
    manage.py  ; omite o manage.py
```
6. Execute novamente `pytest` e verifique que arquivos como `manage.py` não aparecem mais no relatório.

> A partir de agora, sempre execute testes utilizando "pytest".


## Exercício 6 – Múltiplas configurações

Crie diferentes arquivos de configuração para os ambientes de `produção` e `desenvolvimento`. Lembre-se de atualizar os valores que referenciavam o arquivo `settings.py` para agora referenciar um dos arquivos de configuração criados (`asgi.py`, `wsgi.py` e `manage.py`).

Sugestão de estrutura de arquivos:

```
raíz_do_projeto/
|__ tamarcado/ (projeto django)
    |__ settings/
        |__ dev.py
        |__ prod.py
```


## Exercício 7 – Corrigindo nossa variável TESTING

Agora que estamos executando nossos testes simplesmente com o comando `pytest`, nossa variável de configuração `TESTING` não vai estar definida como `True` (pois agora `sys.argv = ["pytest"]`).

Crie um novo arquivo de configuração que herda de `dev.py` e que defina a variável `TESTING = True`. Garanta que essa é a configuração utilizada ao executar testes com `pytest`.


## Exercício 8 – Utilizando variáveis de ambiente (dotenv)

Variáveis de ambientes são utilizadas para armazenar variáveis de configuração, sejam elas sensíveis (como senhas, chaves de acesso) ou não (como URLs para serviços externos).

1. Substitua a URL para a `BrasilAPI` por uma `variável de configuração` (settings). Essa variável deve ser obtida a partir de uma variável de ambiente (adicionada ao `.env`), e caso não seja encontrada, deve então utilizar o valor default: https://brasilapi.com.br/
2. Gere uma **nova secret key** para o Django e salve no arquivo `.env`. Lembre-se de **não versionar o arquivo .env** (adicione ao `.gitignore`).
3. Crie um arquivo `env.example` e adicione nele as variáveis que um desenvolvedor precisaria adicionar ao ambiente (ou ao .env) para executar o projeto com sucesso.

> Para gerar uma nova **secret key** você pode utilizar a biblioteca `secrets` que faz parte da biblioteca padrão do Python

```python
import secrets

print(secrets.token_urlsafe())
```
Créditos: [humberto.io](https://humberto.io/pt-br/blog/tldr-gerando-secret-key-para-o-django/)


## Exercício 9 – Logging

Altere o código que utiliza a BrasilAPI de modo que, caso ocorra um erro na requisição para buscar os feriados nacionais, um *erro* seja loggado. O **cliente não deve ser impedido de realizar o agendamento nesse caso**.

> Não é necessário para realizar o exercício, mas se quiser ver um exemplo de configuração de logs: [exemplo_config_log.py](./exemplo_config_log.py)


## Exercício 10 - Requirements

Crie um arquivo de requirements para o ambiente de desenvolvimento e um para o ambiente de produção.


# Projeto Final: Adicionando endereço ao Prestador

Prestadores de serviço podem ter um `Endereço` associado. O modelo `Endereço` deve possuir:
- CEP
- Estado
- Cidade
- Bairro
- Rua
- Complemento (opcional)

Implemente uma view para criar um `Endereço` associado a um certo prestador através de seu *username*.

Sugestão de contrato:
```
POST /api/prestadores/<pk>/endereços/

{
    "cep": "22220050",
    "estado": "RJ",
    "cidade": "Rio de Janeiro",
    "rua": "Rua dos Pinheiros",
    "complemento": "100"  // Opcional
}
```

Caso o cliente forneça **apenas o CEP**, a sua API deve preencher as outras informações para salvar o modelo `Endereço`. Caso o CEP seja inválido, informar isso ao cliente através de um status code 400.

> Você vai precisar utilizar uma API externa como a [Brasil API](https://brasilapi.com.br/docs#tag/CEP/paths/~1cep~1v1~1{cep}/get) para buscar informações a partir de um CEP fornecido.

> Lembre-se de evitar que requisições sejam feitas para a Brasil API caso estejamos rodando testes!
