from django.db import models
from django.utils import timezone

# Creación de campos de tabla categorías.

class Detalleblog(models.Model):
    detalles = models.CharField(max_length=6000, default='DEFAULT VALUE')
    logo = models.FileField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'detalleblog'
       

# Create your models here.
