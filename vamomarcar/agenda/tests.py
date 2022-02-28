from datetime import date
from django.test import TestCase, Client

from agenda.models import Evento, Categoria


class TestPaginaInicial(TestCase):
    def test_lista_eventos(self):
        client = Client()
        response = client.get("/")
        # print(response.content)
        # self.assertContains(response, "<th>Nome</th>")
        self.assertTemplateUsed(response, "agenda/listar_eventos.html")


class TestListagemDeEventos(TestCase):
    def test_evento_com_data_de_hoje_e_exibido(self):
        categoria = Categoria()
        categoria.name = "Backend"
        categoria.save()

        evento = Evento()
        evento.nome = "Aula de Python"
        evento.categoria = categoria
        evento.local = "Rio de Janeiro"
        evento.data = date.today()
        evento.save()

        client = Client()
        response = client.get("/")
        self.assertContains(response, "Aula de Python")
        self.assertEqual(list(response.context["eventos"]), [evento])

    def test_eventos_sem_data_sao_exibidos(self):
        categoria = Categoria()
        categoria.name = "Backend"
        categoria.save()

        evento = Evento()
        evento.nome = "Aula de Python"
        evento.categoria = categoria
        evento.local = "Rio de Janeiro"
        evento.data = None
        evento.save()

        client = Client()
        response = client.get("/")
        self.assertContains(response, "Aula de Python")
        self.assertContains(response, "A definir")
        self.assertEqual(list(response.context["eventos"]), [evento])