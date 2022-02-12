from datetime import date, timedelta
from django.test import TestCase, Client

from agenda.models import Evento


class TestListarEventos(TestCase):
    """
    Test cases:
    - Se não houver nenhum evento criado, exibe lista vazia (nenhum <tr>)
    - Se houverem apenas eventos criados no passado, exibe lista vazia
        - Ou passa para o contexto um elemento: {"eventos": []} (len == 0)
    - Se houverem eventos criados no futuro, passa para o contexto esses eventos
        - Ou, exibir HTML (mais "chato" porque vamos precisar ficar atualizando nosso teste)
        - Boa prática: não testar constantes, testar comportamentos
    - Utiliza o template correto
    - Retorna 200 caso tudo ocorra bem
    """
    def test_lista_eventos_com_a_data_do_dia_atual(self):
        evento = Evento.objects.create(
            nome="Evento Hoje",
            data=date.today(),
        )
        response = Client().get("/eventos/")
        self.assertIn("Evento Hoje", response.content.decode())

    def test_nao_exibe_eventos_passados(self):
        evento = Evento.objects.create(
            nome="Evento Hoje",
            data=date.today() - timedelta(days=1),  # Ontem
        )
        response = Client().get("/eventos/")
        self.assertNotIn("Evento Hoje", response.content.decode())
        self.assertEqual(len(response.context["eventos"]), 0)