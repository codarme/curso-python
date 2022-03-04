from django.contrib import admin

from agenda.models import Evento, Categoria
# Também podemos usar import relativo
# from .models import Evento, Categoria

admin.site.register(Evento)
admin.site.register(Categoria)