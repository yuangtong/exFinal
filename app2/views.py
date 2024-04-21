from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return HttpResponse("Bienvenidos a App2")

def welcome(request):
    nombreUsuario = "Javier"
    lista_lenguajes = ['Python', 'React', 'Javascript']
    var_selectiva = 'Django'
    return render(request,'welcome.html',{
        'nombreUsuario':nombreUsuario,
        'lista_lenguajes':lista_lenguajes,
        'var_selectiva':var_selectiva
    })

def hola(request,nombrePersona):
    return render(request,'hola.html',{
        'nombrePersona':nombrePersona
    })

#127.0.0.1:8000 / app2 / hola / Alexander