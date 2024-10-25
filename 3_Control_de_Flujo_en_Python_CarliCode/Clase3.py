# Generadores e iteradores

# Creando una lista de numeros del 1 al 4

numeros = [1,2,3,4]

# Creando un iterador a partir de la lista

iterador = iter(numeros)

# Usando next() para obtener los elementos del iterador

print(next(iterador))
print(next(iterador))
print(next(iterador))
print(next(iterador))
#print(next(iterador)) # Genera StopIteration porque no hay mas elementos


# Generadores

# Ejemplo generador de numeros impares:

def generador_impares(limite):
    for numero in range (1, limite +1, 2):
        yield numero

# Usando el generador

for impar in generador_impares(10):
    print(impar)

