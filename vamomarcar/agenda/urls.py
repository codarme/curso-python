from django.urls import path
from .views import exibir_evento

urlpatterns = [
    path('eventos/', exibir_evento),
]
