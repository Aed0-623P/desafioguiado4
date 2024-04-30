from django.db import models
from django.utils import timezone

# Create your models here.

class Vehiculo(models.Model):
    patente = models.CharField(max_length=6, primary_key=True)
    marca = models.CharField(max_length=20, null=False, blank=False)
    modelo = models.CharField(max_length=20, null=False, blank=False)
    year = models.IntegerField(null=False, blank=False)
    activo = models.BooleanField(default=False, null=False, blank=False)

class Chofer(models.Model):
    rut = models.CharField(max_length=9, primary_key=True)
    nombre = models.CharField(max_length=50, null=False, blank=False)
    apellido = models.CharField(max_length=50, null=False, blank=False)
    activo = models.BooleanField(default=False, null=False, blank=False)
    creacion_reg = models.DateField(auto_now_add=False)
    vehiculo_id = models.OneToOneField('Vehiculo', max_length=6, on_delete=models.CASCADE, default="autito", to_field='patente')

class RegistroContabilidad(models.Model):
    fecha_compra = models.DateField(null=False)
    valor = models.FloatField(null=False)
    vehiculo = models.OneToOneField('Vehiculo', max_length=6, on_delete=models.CASCADE, to_field='patente', default="registro")



