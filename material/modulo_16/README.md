# Infraestrutura e configuração

Esse módulo vai falar sobre parte de "infraestrutura": configurando coisas como logging, cobertura de teste, gerenciamento de variáveis de ambiente e valores sensíveis. Além disso, pela primeira vez vamos fazer consultas para uma API Externa e discutir como escrever testes que sejam confiáveis e rápidos para códigos que dependem de componentes externos ao nosso projeto.


## Palavras-chave

- Consumindo outras APIs
- Test Coverage
- Pytest
- Mock/Patch
- Django Settings
- Logging
- dotenv (.env)
- requirements.txt


## Exercícios

Os exercícios podem ser acessados [aqui](./exercícios.md).


## Referências


### Documentações

- [BrasilAPI Docs](https://brasilapi.com.br/docs)
- [Utilizando definições de settings.py](https://docs.djangoproject.com/pt-br/4.0/topics/settings/#using-settings-in-python-code)
- [HOWTO: Logging em Python](https://docs.python.org/pt-br/3/howto/logging.html#basic-logging-tutorial)
- [Logging no Django](https://docs.djangoproject.com/en/4.0/topics/logging/)


### Ferramentas de testes

- [Framework de testes unitários (unittest)](https://docs.python.org/pt-br/3/library/unittest.html)
- [Framework de testes – Pytest](https://docs.pytest.org/en/7.1.x/)
- [Ferramenta para medir Coverage](https://coverage.readthedocs.io/en/6.3.2/)


### Bibliotecas instaladas

- [requests](https://docs.python-requests.org/en/latest/)
- [pytest-django](https://pytest-django.readthedocs.io/en/latest/)
- [pytest-cov](https://pypi.org/project/pytest-cov/)
- [python-dotenv](https://pypi.org/project/python-dotenv/)


### Code snippets

- [Exemplo comentado sobre como/onde fazer o mock.patch](exemplo_patch/tests.py)