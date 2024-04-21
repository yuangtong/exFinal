from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return HttpResponse("Bienvenidos a Django")

def rutaEjemplo(request):
    return HttpResponse("Esta es una segunda ruta de ejemplo")