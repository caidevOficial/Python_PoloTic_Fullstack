from django.http import request
from django.shortcuts import render
from django import forms
from django.urls import reverse
from django.http import HttpResponseRedirect

# Create your views here.
#tasks_list = ["Programar", "Abrir una birrita", "Dormir"]

def index(request):
    if "tasks_list" not in request.session:
        request.session["tasks_list"] = []

    return render(request, "TaskManager/index.html", {
        "tasks":request.session["tasks_list"]
        })

# Agregar nueva tarea: 
def agregar(request):
    if request.method=="POST":
        form = FormNuevaTarea(request.POST)
        if form.is_valid():
            tarea = form.cleaned_data["tarea"]
            # hace los controles necesarios para purgar la informacion
            # y no sea ninguna solicitud extraña
            request.session["tasks_list"] += [tarea]
            return HttpResponseRedirect(reverse("Tasks_App:index"))
            # si todo bien, mando al indice
        else:
            # Redirecciono a Agregar en caso contrario.
            return render(request, "TaskManager/agregar.html", {
                "form": form
            })


    return render(request, "TaskManager/agregar.html", {
        "form" : FormNuevaTarea()
    })

class FormNuevaTarea(forms.Form):
    """FormNuevaTarea PAra escribir en el form."""
    tarea = forms.CharField(label="Ingrese Tarea")