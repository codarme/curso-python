from django.urls import path
from .views import exibir_evento, listar_eventos


urlpatterns = [
    path('eventos/<int:id>/', exibir_evento),
    path('eventos/', listar_eventos),
]
