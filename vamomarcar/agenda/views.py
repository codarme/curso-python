from django.shortcuts import render
from agenda.models import Evento


aula_python = dict(nome="Aula de Python", categoria="Backend", local="Rio de Janeiro")
aula_js = dict(nome="Aula de JavaScript", categoria="Fullstack", link="http://tamarcado.com/js")
eventos = [
    aula_python,
    aula_js,
]

def exibir_evento(request):
    return render(request, "agenda/exibir_evento.html", context={"evento": eventos[0]})