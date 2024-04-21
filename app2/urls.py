from django.urls import path
from . import views

app_name='app2'

urlpatterns = [
    path('',views.index,name='index'),
    path('welcome',views.welcome,name='welcome'),
    path('hola/<str:nombrePersona>',views.hola,name='hola')
]