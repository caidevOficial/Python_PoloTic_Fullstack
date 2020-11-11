import sys

try: # trato de abrir el archivo y escribirle algo
    archivo = open("Ejercicio04.txt")
    archivo.write("#Team Carpincho!")
except: # si hubo problema al abrir, mando mensaje de error
    print("Error al abrir el archivo")
finally: # Finalmente cierro el archivo Siempre para liberar memoria
    archivo.close()