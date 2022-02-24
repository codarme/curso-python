class Tarefa:
    def __init__(self, titulo, descricao="", data=None, notificacao=None, concluida=False, prioridade=0):
        self.titulo = titulo
        self.descricao = descricao
        self.data = data
        self.notificacao = notificacao
        self.concluida = concluida
        self.prioridade = prioridade

    def concluir(self):
        self.concluida = True

    def adicionar_descricao(self, descricao):
        self.descricao = descricao

    def adiar_notificacao(self, minutos):
        """
        Adia a notificação em uma certa quantidade de minutos
        """
        pass

    def atrasada(self):
        """
        Diz se tarefa está atrasada. Ou seja, data < hoje
        """
        pass



class ListaDeTarefas:
    def __init__(self):
        """
        _atributo indica que "_atributo" não deve ser utilizado diretamente fora dessa classe.
        Vamos criar métodos que retornam esses atributos de acordo com uma lógica.
        """
        self._tarefas = []
        self._quantidade_tarefas = 0

    def get_tarefas(self, incluir_concluidas=False):
        pass

    def get_tarefas_atrasadas(self):
        pass

    