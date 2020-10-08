def cuadrado(x):
    return x*x

print("Sin usar lambda: ")
print(cuadrado(5))

varCuadrado = lambda x: x*x
print("usando Lambda: ")
print(varCuadrado)