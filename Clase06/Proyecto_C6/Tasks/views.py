from django.shortcuts import render

# Create your views here.
tasks = ["Estudiar","Tomar Cafe", "Dormir"]

def index(request):
    return render(request, "Tasks/index.html", {"Tasks":tasks})