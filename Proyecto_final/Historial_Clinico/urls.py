#TODO hacer las vistas
from django.urls import path
from . import views 

app_name = 'HC_App'
urlpatterns = [
    path('Historial_Clinico/', views.index, name='index'),
]
