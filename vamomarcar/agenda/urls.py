from django.urls import path
from .views import exibir_evento, participar_de_evento, listar_eventos


urlpatterns = [
    path('eventos/<int:id>/', exibir_evento, name='exibir_evento'),
    path('eventos/', listar_eventos, name='listar_eventos'),
    path('participar/', participar_de_evento, name='participar_de_evento')
]
