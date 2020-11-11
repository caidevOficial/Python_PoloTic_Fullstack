import sys 
# Tiene funciones relacionadas al sistema para terminar la ejecucion
# ante un error.
#############################################################
# Con el afan de capturar los errores, usamos las excepciones
try: # intentara ejecutar las lineas de abajo
    numero1 = int(input("ingrese el numero 1: "))
    numero2 = int(input("ingrese el numero 2: "))
except ValueError: # en caso de hallar un error determinado, ejecutara el mensaje.10
    print("#### Valor no valido ####")
    sys.exit(1) # termina la ejecucion al haber un error.

try:
    divResultado = numero1/numero2
    error = 0
except ZeroDivisionError:
    print("#### Error! No se puede dividir por cero! ####")
    error = 1
    sys.exit(1) # termina la ejecicion al haber un error.
else: # Se ejecuta si no se producieron errores.
    print(f"El resultado de la operacion {numero1} / {numero2} = {divResultado}")
finally: # Se ejecuta independientemente de si fallo o no.
    print(f"Mensaje de error = {error}")
    print("-------------- Execution done! --------------")
