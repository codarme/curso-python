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