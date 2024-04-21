from django.db import models

# Create your models here.
class personas(models.Model):
    nombre = models.CharField(max_length=32, null=True, blank=True)
    apellido = models.CharField(max_length=32, null=True, blank=True)
    fecha = models.CharField(max_length=32, null=True, blank=True)
    tipoPersona = models.CharField(max_length=32, null=True, blank=True)
    codigoPersona = models.CharField(max_length=32, null=True, blank=True)

class datosAdicionales(models.Model):
    telefono = models.CharField(max_length=32, null=True, blank=True)
    residencia = models.CharField(max_length=32, null=True, blank=True)
    personaRel = models.OneToOneField(personas, null=True, blank=True, on_delete=models.CASCADE)

class tareasxPersona(models.Model):
    nombre = models.CharField(max_length=32, null=True, blank=True)
    descripcion = models.CharField(max_length=32, null=True, blank=True)
    personaRel= models.ForeignKey(personas,null=True, blank=True, on_delete=models.SET_NULL)