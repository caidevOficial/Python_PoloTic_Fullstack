from django.db import models
from django.db.models.deletion import CASCADE
from Pedido.models import Pedido as PDD

# Create your models here.
class Producto(models.Model):
    # Constantes
    LEJOS = 'LJ'
    CERCA = 'CE'
    DISTANCIA = (
        (LEJOS, 'Lejos'),
        (CERCA, 'Cerca'),
    )

    IZQUIERDA = 'IZ'
    DERECHA = 'DE'
    FOCAL = (
        (IZQUIERDA, 'Izuquierda'),
        (DERECHA, 'Derecha'),
    )

    id_producto = models.IntegerField(primary_key=True, default=0)
    id_Pedido = models.ForeignKey(PDD, on_delete=CASCADE)
    descripcion = models.TextField(max_length=35)
    precio = models.FloatField()
    esLente = models.BooleanField(default='False')
    distaciaLente = models.CharField(max_length=2, choices=DISTANCIA, default="")
    tipoFocal = models.CharField(max_length=2, choices=FOCAL, default="")
    tieneArmazon = models.BooleanField(default='False')