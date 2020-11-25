from django.urls import path
from . import views 
# importo todo lo que hay dentro de views
# Crear una variable que sera los patrones de url que va a recibir
# el navegador.
# El server tomara la lista y lo va a mandar a que lo procese lo que 
# esta dentro de views.py

# Setear aca todas las urls de la aplicacion
app_name = 'Aerolinea'
urlpatterns = [
    path("", views.index, name="index"),
]