from django.db.models.deletion import CASCADE
from Paciente.models import Paciente as PC
from PersonalMedico.models import PersonalMedico as PM
from django.db import models
from django.db.models import Model as MD 

# Create your models here.
class Turno(MD):
    # Atributos
    fecha = models.DateTimeField(blank=False,null=False)
    estado = models.BooleanField
    id_medico = models.ForeignKey(PM,on_delete=CASCADE) # Medico
    tomado_por = models.ForeignKey(PC,on_delete=CASCADE) # Paciente

    # Metodos
    def __init__(self, fecha, estado, id_medico, tomado_por):
        self.fecha = fecha
        self.estado = estado
        self.id_medico = id_medico
        self.tomado_por = tomado_por
    
    def agregarTurno(self):
        pass

    def modificarTurno(self):
        pass

    def borrarTurno(self):
        pass
