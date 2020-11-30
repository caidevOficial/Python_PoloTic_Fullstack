#TODO hacer las vistas
from django.urls import path
from . import views 

from Historial_Clinico import views as HC_views

app_name = 'Paciente_App'
urlpatterns = [
    path('index', views.index, name='index'),
    path('/Historial-Clinico', HC_views.index, name='hc_index'),
]
