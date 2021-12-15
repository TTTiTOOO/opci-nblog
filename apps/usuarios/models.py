from django.db import models
from django.utils import timezone

# Creación de campos de tabla usuarios.

class Usuarios(models.Model):
    nombre = models.CharField(max_length=1000, default='DEFAULT VALUE')
    img = models.FileField()
    web = models.CharField(max_length=700, default='DEFAULT VALUE')
    descripcion = models.TextField()
    slug = models.CharField(max_length=5000, default='DEFAULT VALUE')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'usuarios'
