from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def index(request):
    # recibo la request del http
    #return HttpResponse("<h1 style=\"color:darkblue\">¡Ohayou Sekai!</h1>")
    return render(request, "hola/index.html")

def saludar(request,nombre):
    #return HttpResponse(f"¡Ohayou {nombre.capitalize()}!") 
    #respuesta general para cada usuario (primera letra en mayuscula)
    return render(request, "hola/saludar.html",{"nombre":nombre.capitalize()
    })

