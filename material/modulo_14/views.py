from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from rest_framework.decorators import api_view

from agenda.models import Agendamento
from agenda.serializers import AgendamentoSerializer

# TODO: criar o modelo Agendamento (e fazer as migrações)
# TODO: criar o serializer AgendamentoSerializer com os campos corretos.
# TODO: finalizer a implementação dos métodos (views) abaixo.

@api_view(http_method_names=["GET"])
def agendamento_detail(request, id):
    obj = get_object_or_404(Agendamento, id=id)
    if request.method == "GET":
        # Buscar instância de Agendamento
        agendamento = {}
        # Instanciar serializer passando a instância de Agendamento
        serializer = AgendamentoSerializer(agendamento)
        # Retornar JsonResponse com os dados do serializer
        return JsonResponse(serializer.data, status=200)


@api_view(http_method_names=["GET", "POST"]) 
def agendamento_list(request):
    if request.method == "GET":
        queryset = []  # TODO: buscar todos Agendamentos registrados
        serializer = AgendamentoSerializer(queryset, many=True)  # many=True indica que o objeto sendo serializado é uma coleção
        return JsonResponse(serializer.data, safe=False)  # safe=False: permite serialização de objetos que não são dicionários (lista)
    if request.method == "POST":
        data = request.data
        # Criar serializer a partir de `data`
        serializer = ...
        if serializer.is_valid():
            validated_data = serializer.validated_data
            Agendamento.objects.create(...)  # TODO: criar instância de Agendamento com valores validados.
            return JsonResponse(serializer.data, status=201)
        # TODO: retornar JsonResponse com os erros do serializer e status 400
        return JsonResponse("IMPLEMENTAR")
