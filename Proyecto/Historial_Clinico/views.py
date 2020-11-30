from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request,"Historial_Clinico/index.html")

def ver(request):
    return render(request,"Historial_Clinico/ver.html")