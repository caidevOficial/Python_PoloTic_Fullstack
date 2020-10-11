from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def index(request):
    # recibo la request del http
    return HttpResponse("¡Ohayou Sekai!")

def saludar(request,nombre):
    return HttpResponse(f"¡Ohayou {nombre.capitalize()}!") 
    #respuesta general para cada usuario (primera letra en mayuscula)

