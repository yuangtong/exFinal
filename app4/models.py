from django.db import models
from datetime import date
from django.contrib.auth.models import User

# Create your models here.
class datosUsuario(models.Model):
    userRel = models.OneToOneField(User,on_delete=models.CASCADE)
    nroCelular = models.CharField(max_length=16, null=True, blank=True)
    profesionUsuario = models.CharField(max_length=64, null=True, blank=True)
    perfilUsuario = models.CharField(max_length=512, null=True, blank=True)
    fechaCreacion = models.DateField(default=date.today)

class tareasSistem(models.Model):
    nombreTarea = models.CharField(max_length=32, null=True, blank=True)
    descripcionTarea = models.CharField(max_length=512, null=True, blank=True)
    fechaFin = models.DateField(default=date.today)
    fechaInicio = models.DateField(default=date.today)
    estadoTarea = models.CharField(max_length=16, null=True, blank=True)
    usuarioCreador = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    usuarioResponsable = models.ForeignKey(datosUsuario, on_delete=models.SET_NULL, null=True, blank=True)

class comentarioTarea(models.Model):
    tareaRelacionada = models.ForeignKey(tareasSistem,on_delete=models.CASCADE)
    usuarioRelacionado = models.ForeignKey(User,on_delete=models.CASCADE)
    comentario = models.CharField(max_length=512, null=True, blank=True)