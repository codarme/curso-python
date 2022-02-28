import unittest
from datetime import datetime
from tarefa import Tarefa


class TestConcluir(unittest.TestCase):
    def test_concluir_tarefa_altera_concluido_para_true(self):
        tarefa = Tarefa("Estudar Python")
        tarefa.concluir()
        self.assertEqual(tarefa.concluida, True)

    def test_concluir_tarefa_concluida_mantem_concluida_como_true(self):
        tarefa = Tarefa("Estudar Python")
        tarefa.concluir()
        self.assertEqual(tarefa.concluida, True)
        tarefa.concluir()
        self.assertEqual(tarefa.concluida, True)


class TestAdiarNotificacao(unittest.TestCase):
    def test_adia_notificacao_em_N_minutos(self):
        dt_original = datetime(2022, 2, 10, 9, 10)  # year, month, day, hour, minute, second, millisecond
        tarefa = Tarefa("Estudar Python", data_notificacao=dt_original)
        tarefa.adiar_notificacao(15)

        dt_esperado = datetime(2022, 2, 10, 9, 25)
        self.assertEqual(tarefa.data_notificacao, dt_esperado)



unittest.main()