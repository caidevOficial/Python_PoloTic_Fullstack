#TODO hacer las vistas
from django.urls import path
from . import views 

app_name = 'PM_App'
urlpatterns = [
    path('PersonalMedico/', views.index, name='index'),
]