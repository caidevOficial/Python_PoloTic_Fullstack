guerreros = [
    {"Nombre":"Kakaroto", "Raza":"Saiyajin"},
    {"Nombre":"Vegita", "Raza":"Saiyajin"},
    {"Nombre":"Beerus", "Raza":"HakaiNoKami"},
    {"Nombre":"Whiss", "Raza":"Tenshi"},
    {"Nombre":"Burorii", "Raza":"Saiyajin"},
]

# Creo una funcion que me traiga el item Nombre para ordenar.
def funcion(unGuerrero):
    return unGuerrero["Nombre"]

# Al pasarle la key de la funcion, ordenara por nombre.
#guerreros.sort(key=funcion)


# Funcion con lambda: es una forma de definir una funcion en menos lineas
guerreros.sort(key=lambda unGuerrero: unGuerrero["Raza"])

# Imprimo nombres
print(guerreros)