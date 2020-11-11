"""Proyecto_C6 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

from django.config import settings
from django.config.urls.static import static

# Setear aca las distintas urls del proyecto
urlpatterns = [
    path('admin/', admin.site.urls),
    path('Tasks/',include("Tasks.urls")),
    path('NewYear/',include("NewYear.urls")),
    path('hola/', include("PythonFT.urls")) # le permite que acceda al url.py de la app

] +static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
