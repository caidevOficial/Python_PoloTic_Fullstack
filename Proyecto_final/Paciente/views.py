from Paciente.models import Paciente
from django.http import request
from django.shortcuts import render
from django.utils import timezone
from .models import Paciente

# Create your views here.
def index(request):
    return render(request,"Paciente/index.html")

def verPaciente(request):
    orden = Paciente.objects.order_by('horario')
    return render(request, "Paciente/index.html", {'ordenadoHorario':orden})
