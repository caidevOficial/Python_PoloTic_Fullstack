from django.http.response import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from django.contrib.auth import authenticate, login, logout

# Create your views here.
def index(request):
    if not request.user.is_authenticated:
        # si no esta logeado, lo lleva al login
        return HttpResponseRedirect(reverse("login"))
    return render(request, 'Usuario/Usuarios.html')

def login(request):
    pass

def logout(request):
    pass
