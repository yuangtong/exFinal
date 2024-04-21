from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
from .models import personas, datosAdicionales

# Create your views here.
def index(request):
    personasTotales = personas.objects.all()
    return render(request,'index.html',{
        'personasTotales':personasTotales
    })

def nuevoUsuario(request):
    if request.method == 'POST':
        nombre = request.POST.get('nombre')
        apellido = request.POST.get('apellido')
        fechaNacimiento = request.POST.get('fecha')
        tipoPersona = request.POST.get('tipo')
        codigoPersona = request.POST.get('codigo')
        telefono = request.POST.get('telefono')
        residencia = request.POST.get('residencia')
        
        personaCreada = personas.objects.create(
            nombre=nombre,
            apellido=apellido,
            fecha=fechaNacimiento,
            tipoPersona=tipoPersona,
            codigoPersona=codigoPersona
        )

        datosAdicionales.objects.create(
            telefono=telefono,
            residencia=residencia,
            personaRel=personaCreada
        )

        return HttpResponseRedirect(reverse('app3:index'))
    return render(request,'nuevoUsuario.html')

def verTareas(request,idPersona):
    personaInfo = personas.objects.get(id=idPersona)
    tareasxUsuario = personaInfo.tareasxpersona_set.all()
    return render(request,'verTareas.html',{
        'tareasxUsuario':tareasxUsuario
    })