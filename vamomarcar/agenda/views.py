from datetime import date
from django.http.response import Http404, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
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
        data__lt=date.today()
    ).order_by("data")

    return render(request, "agenda/listar_eventos.html", context={"eventos": eventos})

def participar_de_evento(request):
    if request.method == "POST":
        evento_id = request.POST.get("evento_id")
        evento = get_object_or_404(Evento, pk=evento_id)
        evento.participantes += 1
        evento.save()
        # É uma boa prática retornar um HttpResponseRedirect após lidar com POST para
        # evitar operações "duplicadas", por exemplo, se o usuário recarregar a página após
        # o POST, o Chrome vai enviar um novo POST (pois "recarregar" na verdade é realizar
        # a última operação bem sucedida).
        return HttpResponseRedirect(reverse('exibir_evento', args=(evento_id,)))
        # return render(request, "agenda/exibir_evento.html", context={"evento": evento})