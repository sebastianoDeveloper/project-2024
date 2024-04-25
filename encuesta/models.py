from django.db import models

# Create your models here.
class Informacion(models.Model):
    TRANSPORTE_CHOICES = [
        ('Tren', 'Tren'),
        ('Corredor', 'Corredor'),
        ('Metropolitano', 'Metropolitano'),
    ]

    nombre = models.CharField(max_length=40)
    transporte = models.CharField(max_length=20, choices=TRANSPORTE_CHOICES)
    horario = models.TimeField()
    dni = models.IntegerField()
    edad = models.IntegerField()
