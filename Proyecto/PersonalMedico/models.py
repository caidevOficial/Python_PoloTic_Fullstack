from django.db.models.deletion import CASCADE
from Paciente.models import Paciente
from django.db import models
from django.db.models import Model as MD 

# Create your models here.
class PersonalMedico(MD):
    # Atributos
    id_PersonalMedico=models.IntegerField(primary_key=True,default=0)
    nombre=models.CharField(max_length=35,null=False,default="")
    apellido=models.CharField(max_length=45,null=False,default="")
    id_grupoEmpleado = models.IntegerField
    legajo_empleado = models.CharField(max_length=10)
    id_pacienteAsignado=models.ForeignKey(Paciente,on_delete=CASCADE)

    # Metodos
    def __init__(self, nombre, apellido, id_grupoEmple, legajo, id_pacienteAsignado):
        self.nombre = nombre
        self.apellido = apellido
        self.id_grupoEmpleado = id_grupoEmple
        self.legajo_empleado = legajo
        self.id_pacienteAsignado = id_pacienteAsignado

    def verPacientes(self):
        paciente_id = self.id_pacienteAsignado
        return paciente_id
    
    def agregarObservaciones(self):
        pass
