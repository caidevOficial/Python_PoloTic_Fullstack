from django.http.response import HttpResponseRedirect
from Aerolinea.models import Aerolinea, Aeropuerto, Pasajero
from django.shortcuts import render
from django.urls import reverse

# Create your views here.
def index(request):
    return render(request,"Aerolinea/index.html", {
        "Aerolinea": Aerolinea.objects.all()
    })

def vuelo(request, vuelo_id):
    unVuelo = Aerolinea.objects.get(id=vuelo_id)
    pasajeros = unVuelo.pasajeros.all()
    noSonPasajeros = Pasajero.objects.exclude(vuelos=unVuelo).all()
    return render(request, "Aerolinea/vuelo.html", {
        "vuelo":unVuelo,
        "pasajeros":pasajeros,
        #"pasajeros":noSonPasajeros
    })

def reservar(request, id_vuelo):
    if request.method == "post":
        unVuelo = Aerolinea.objects.get(pk=id_vuelo)
        pasajero_id = int(request.POST["pasajero"])
        unPasajero = Pasajero.objects.get(pk=pasajero_id)
        unPasajero.Aerolinea.add(unVuelo)
        return HttpResponseRedirect(reverse("Aerolinea", args=(unVuelo.id,)))