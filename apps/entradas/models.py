from django.db import models
from django.utils import timezone

# Creación de campos de tabla entradas.

class Entradas(models.Model):
    titulo = models.CharField(max_length=5000, default='DEFAULT VALUE')
    contenido = models.TextField()
    slug = models.CharField(max_length=5000, default='DEFAULT VALUE')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'entradas'
