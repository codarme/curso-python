from django.db import models

class Evento(models.Model):
    # Primary Key (pk) é criada automaticamente
    nome = models.CharField(max_length=256)
    categoria = models.ForeignKey("Categoria", on_delete=models.SET_NULL, null=True)
    local = models.CharField(blank=True, max_length=256)
    link = models.URLField(blank=True, max_length=256)


class Categoria(models.Model):
    CATEGORIAS = [
        ("Backend", "Backend"),
        ("Frontend", "Frontend"),
        ("Fullstack", "Fullstack"),
        ("UX/UI", "UX/UI"),
    ]

    nome = models.CharField(unique=True, max_length=256, choices=CATEGORIAS)