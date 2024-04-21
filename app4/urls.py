from django.urls import path
from . import views

app_name='app4'

urlpatterns = [
    path('',views.index,name='index'),
    path('perfilUsuario',views.perfilUsuario,name='perfilUsuario'),
    path('consolaAdministrador',views.consolaAdministrador,name='consolaAdministrador'),
    path('cerrarSesion',views.cerrarSesion,name='cerrarSesion'),
    path('finalizarTarea/<str:idTarea>',views.finalizarTarea,name='finalizarTarea'),
    path('ejemploJs',views.ejemploJs,name='ejemploJs'),
    path('devolverMensaje',views.devolverMensaje,name='devolverMensaje'),
    path('conseguirInfoTarea',views.conseguirInfoTarea,name='conseguirInfoTarea'),
    path('publicarComentario',views.publicarComentario,name='publicarComentario'),
    path('react1',views.react1,name='react1')
]