#TODO hacer las vistas
from django.urls import path
from . import views 

app_name = 'Turno_App'
urlpatterns = [
    path('index', views.index, name='index'),
    path('/VerTurnos', views.verTurnos, name='ver'),   
]
