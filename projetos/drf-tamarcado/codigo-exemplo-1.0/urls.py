from django.urls import path
from agenda.views import agendamento_detail, agendamento_list

urlpatterns = [
    path('agendamentos/', agendamento_list),
    path('agendamentos/<int:id>/', agendamento_detail)
]
