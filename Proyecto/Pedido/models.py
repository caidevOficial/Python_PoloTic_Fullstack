from django.db import models
from django.db.models.deletion import CASCADE
from Paciente.models import Paciente as PTT

# Create your models here.
class Pedido(models.Model):
    # Constantes
    TARJETA_CRED = 'TC'
    DEBITO = 'DE'
    BILLETERA_VIRT = 'BV' 
    EFECTIVO = 'EF'
    TIPO_PAGO = (
        (TARJETA_CRED, 'Tarjeta de Credito'),
        (DEBITO, 'Tarjeta de Debito'),
        (BILLETERA_VIRT, 'Billetera Virtual'),
        (EFECTIVO, 'Efectivo'),
    )
    FINALIZADO = 'FI'
    PROCESANDO = 'PR'
    ESTADO_PEDIDO = (
        (FINALIZADO, 'Finalizado'),
        (PROCESANDO, 'Procesando'),
    )

    # Atributos
    id_Pedido = models.IntegerField(primary_key=True, default=0)
    id_Paciente = models.ForeignKey(PTT, on_delete=CASCADE)
    id_Producto = models.IntegerField()
    cantidad_Prod = models.IntegerField()
    subTotal = models.FloatField()
    total = models.FloatField()
    tipoPago = models.CharField(max_length=2, choices=TIPO_PAGO, default=EFECTIVO)
    estadoPedido = models.CharField(max_length=2, choices=ESTADO_PEDIDO, default=PROCESANDO)

    # Metodos