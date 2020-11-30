from django.db.models.deletion import CASCADE
from django.contrib.admin.sites import DefaultAdminSite
from django.db import models
from django.db.models.fields import DateTimeField
from django.utils import timezone
from django.utils.timezone import now
from django.db.models import Model as MD 

class Paciente(MD):

    # Atributos
    id_paciente=models.IntegerField(primary_key=True,default=0)
    nombre=models.CharField(max_length=35,null=False,default="")
    apellido=models.CharField(max_length=45,null=False,default="")
    dni=models.CharField(max_length=10,null=False,default="")
    registro=models.DateTimeField(default=timezone.now)
    horario=models.DateTimeField(blank=True,null=True)
    
    #Metodos
    def __init__(self, idPaciente, nombre, apellido, dni, registro, horario):
        self.id_paciente = idPaciente
        self.nombre = nombre
        self.apellido = apellido
        self.dni = dni
        self.registro = registro
        self.horario = horario
    
    def __str__(self):
        return self.nombre and self.apellido

    def ordenPorHorarioRegistro(self):
        sorted(self.horarioRegistro)

    def publicado(self):
        self.horario=timezone.now()
        self.save # guarda el momento del UTC
