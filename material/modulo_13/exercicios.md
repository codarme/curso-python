# Exercícios – Módulo 13 – Testes
1. Faça a implementação dos métodos `multiplicar` e `subtrair` do módulo [calculadora.py](calculadora/calculadora.py). Escreva [testes](calculadora/test_calculadora.py) para sua implementação.
2. Finalize a implementação das classes [ListaDeTarefas](lista_de_tarefas/lista_de_tarefas.py) e [Tarefa](lista_de_tarefas/tarefa.py). Escreva testes para sua implementação.
3. Implemente uma classe segundo a especificação em [calculadora_de_notas.py](calculadora_de_notas/calculadora_de_notas.py). Crie um arquivo de testes e adicione casos de teste para os métodos.
4. Escreva os testes para o sistema implementado no [módulo 12](../modulo_12/exercicios.md).
   - Tanto as `views` quando os métodos adicionados aos `models` (por exemplo, `Evento.cria_evento`) devem ter testes.
   - Para testar que uma função lançou uma exceção, você pode utilizar: `self.assertRaises(ClasseDaExceção, função, arg1, arg2, ...)`
5. Escolha alguns exercícios já implementados na últimas aulas e tente escrever testes para eles. Preferencialmente crie os arquivos de teste ao lado do módulo com a implementação.