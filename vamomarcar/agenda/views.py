from datetime import date
from django.http.response import Http404
from django.shortcuts import render
from agenda.models import Evento


def exibir_evento(request, id):
    try:
        evento = Evento.objects.get(id=id)
    except Evento.DoesNotExist:
        raise Http404("Evento não existe")
    return render(request, "agenda/exibir_evento.html", context={"evento": evento})


def listar_eventos(request):
    # filter vai incluir apenas os objetos que atendam aos critérios do filtro
    # eventos = Evento.objects.filter(
    #     data__gte=date.today()
    # )

    # exclude vai remover os objetos que atendam aos critérios do filtro
    eventos = Evento.objects.exclude(
        data__lte=date.today()
    ).order_by("data")

    return render(request, "agenda/listar_eventos.html", context={"eventos": eventos})