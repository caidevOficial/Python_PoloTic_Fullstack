from Paciente.models import Paciente as PC
from django.db import models
from django.db.models import Model as MD
from django.db.models.deletion import CASCADE
from django.db.models.fields import CharField
from django.db.models.fields.related import ForeignKey

# Create your models here.

class Historial_Clinico(MD):
    id_Historial = models.IntegerField(primary_key=True,default=0)
    fechaObservacion = models.DateTimeField()
    observacion = models.TextField(max_length=200)
    id_Paciente = models.ForeignKey(PC, on_delete=CASCADE)
    
    def __init__(self, id_Histo, fecha, observacion, idPaciente):
        self.id_Historial = id_Histo
        self.fechaObservacion = fecha
        self.observacion = observacion
        self.id_Paciente = idPaciente
