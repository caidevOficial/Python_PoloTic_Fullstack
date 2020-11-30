from Aerolinea.models import Aerolinea
from Aerolinea.models import Aeropuerto
from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request,"Aerolinea/index.html", {
        "Aerolinea": Aerolinea.objects.all()
    })