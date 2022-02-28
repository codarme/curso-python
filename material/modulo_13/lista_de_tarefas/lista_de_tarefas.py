class ListaDeTarefas:
    def __init__(self):
        """
        _atributo indica que "_atributo" não deve ser acessado diretamente fora dessa classe.
        Vamos criar métodos que retornam esses atributos de acordo com uma certa lógica.
        """
        self._tarefas = []
        self._quantidade_tarefas = 0
    
    def adicionar_tarefa(self, tarefa):
        """
        Adiciona uma tarefa na lista (_tarefas.append).
        """
        self._tarefas.append(tarefa)

    def get_tarefas(self, incluir_concluidas=False):
        """
        Retorna lista de tarefas restantes.
        Se incluir_concluidas for passado como True, inclui as tarefas concluídas.
        """
        tarefas_nao_concluidas = []
        for tarefa in self._tarefas:
            if not tarefa.concluida:
                tarefas_nao_concluidas.append(tarefa)
        return tarefas_nao_concluidas


    def get_tarefas_atrasadas(self):
        """
        Retorna a lista de tarefas atrasadas. Ver método: Tarefa.atrasada.
        """
        pass

    def get_tarefas_para_hoje(self):
        """
        Retorna a lista de tarefas que tenham data = hoje.
        """
        pass
    