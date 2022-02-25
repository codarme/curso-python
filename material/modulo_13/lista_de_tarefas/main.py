class Tarefa:
    def __init__(self, titulo, descricao="", data=None, notificacao=None, concluida=False):
        self.titulo = titulo
        self.descricao = descricao
        self.data = data
        self.notificacao = notificacao
        self.concluida = concluida

    def concluir(self):
        """
        Define essa tarefa como concluida.
        """
        pass

    def adicionar_descricao(self, descricao):
        """
        Adiciona uma descrição para a tarefa.
        """
        pass

    def adiar_notificacao(self, minutos):
        """
        Adia a notificação em uma certa quantidade de minutos.
        """
        pass

    def atrasada(self):
        """
        Diz se tarefa está atrasada. Ou seja, data < hoje.
        """
        pass



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
        pass

    def get_tarefas(self, incluir_concluidas=False):
        """
        Retorna lista de tarefas restantes.
        Se incluir_concluidas for passado como True, inclui as tarefas concluídas.
        """
        pass

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
    