# Exercícios – Módulo 13 – Testes
1. Faça a implementação dos métodos `multiplicar` e `subtrair` do módulo [calculadora.py](calculadora/calculadora.py). Escreva [testes](calculadora/test_calculadora.py) para sua implementação.
2. Finalize a implementação das classes [ListaDeTarefas](lista_de_tarefas/lista_de_tarefas.py) e [Tarefa](lista_de_tarefas/tarefa.py). Escreva testes para sua implementação.
3. Implemente uma classe segundo a especificação em [calculadora_de_notas.py](calculadora_de_notas/calculadora_de_notas.py). Crie um arquivo de testes e adicione casos de teste para os métodos.
4. *OPCIONAL*. Escolha alguns exercícios já implementados na últimas aulas e tente escrever testes para eles. Preferencialmente crie os arquivos de teste ao lado do módulo com a implementação.

## Testes para o projeto "vamomarcar" (módulo 12)
- Escreva os testes para o sistema implementado no [módulo 12](../modulo_12/exercicios.md).
- Tanto as `views` quanto os métodos adicionados aos `models` (por exemplo, `Evento.cria_evento`) devem ter testes.
- Para testar que uma função lançou uma exceção, você pode utilizar: `self.assertRaises(ClasseDaExceção, função, arg1, arg2, ...)`

### Casos de teste
Você pode pensar em diversos casos de teste para implementar, segue algumas sugestões:
- Quando não há eventos registrados, `listar_eventos` deve exibir uma tabela vazia (ou contexto vazio).
- Quando há somente eventos com data no passado registrados, `listar_eventos` deve exibir uma tabela vazia (ou contexto vazio).
- Quando há eventos com datas no passado, hoje e no futuro, deve exibir conforme especificação.
- Testar o *happy path* (caminho esperado) para `exibir_evento`
- `exibir_evento` deve retornar `404` quando o evento não existe (por exemplo, é passado um `id` inexistente na requisição).
  - Dica: você pode utilizar `response.status_code` para verificar o código de status de uma resposta.


# Referências
- [Principais métodos de `assert`](./métodos-assert.png)
- [Mais métodos de `assert` da biblioteca `unittest`](https://docs.python.org/pt-br/3/library/unittest.html#unittest.TestCase.assertEqual)
- [Datetime do Python](https://docs.python.org/pt-br/3/library/datetime.html)
- [Exemplos com timedelta](https://docs.python.org/pt-br/3/library/datetime.html#examples-of-usage-timedelta)
- [Utilizando o `client.post` do Django](https://docs.djangoproject.com/en/4.0/topics/testing/tools/#overview-and-a-quick-example)