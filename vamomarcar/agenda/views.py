from django.http.response import Http404
from django.shortcuts import render
from agenda.models import Evento


def exibir_evento(request, id):
    try:
        evento = Evento.objects.get(id=id)
    except Evento.DoesNotExist:
        raise Http404("Evento não existe")
    return render(request, "agenda/exibir_evento.html", context={"evento": evento})