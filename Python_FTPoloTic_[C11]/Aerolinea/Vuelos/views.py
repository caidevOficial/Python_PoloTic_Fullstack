from django.http.response import HttpResponseRedirect
from Vuelos.models import Pasajero, Vuelos
from django.shortcuts import render
from django.urls import reverse

# Create your views here.
def index(request):
    return render(request,"Aerolinea/index.html", {
        "Aerolinea": Vuelos.objects.all()
    })

def vuelo(request, vuelo_id):
    unVuelo = Vuelos.objects.get(id=vuelo_id)
    pasajeros = unVuelo.pasajeros.all()
    noSonPasajeros = Pasajero.objects.exclude(vuelos=unVuelo).all()
    return render(request, "Aerolinea/vuelo.html", {
        "vuelo":unVuelo,
        "pasajeros":pasajeros,
        #"pasajeros":noSonPasajeros
    })

def reservar(request, id_vuelo):
    if request.method == "post":
        unVuelo = Vuelos.objects.get(pk=id_vuelo)
        pasajero_id = int(request.POST["pasajero"])
        unPasajero = Pasajero.objects.get(pk=pasajero_id)
        unPasajero.Vuelos.add(unVuelo)
        return HttpResponseRedirect(reverse("Aerolinea", args=(unVuelo.id,)))