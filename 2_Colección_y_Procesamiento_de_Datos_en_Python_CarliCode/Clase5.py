# List Comprehensions

# Cuadrados de numero del 1 al 10

# Codigo tradicional

cuadrados = []

for x in range (1,11):
    cuadrados.append(x ** 2)
    print(cuadrados)

# List Comprehension

cuadrados = [x ** 2 for x in range (1,11)]
print(cuadrados)


# Convertir grados Celsius a Fahrenheit

# Codigo tradicional

celsius = [0,10,20,30,40]
fahrenheit = []

for temp in celsius:
    fahrenheit.append((temp * 9/5)+32)
    print(fahrenheit)


# List Comprehension

celsius = [0,10,20,30,40]
fahrenheit = [(temp * 9/5)+32 for temp in celsius]
print(fahrenheit)


# Numeros pares del 1 al 20

# Codigo tradicional

pares = []
for x in range (1,21):
    if x % 2 == 0:
        pares.append(x)
        print(pares)

# List Comprehension

pares = [x for x in range (1,21) if x % 2 == 0]
print(pares)


# Matrices y List Comprehensions

# Codigo tradicional

matriz = [[1,2,3],[4,5,6],[7,8,9]]
transpuesta = []
for i in range (3):
    fila = []
    for fila_original in matriz:
        fila.append(fila_original[i])
        transpuesta.append(fila)
        print(transpuesta)


# List Comprehension

matriz = [[1,2,3],[4,5,6],[7,8,9]]

transpuesta = [[fila[i]for fila in matriz] for i in range (3)]
print(transpuesta)


# Numeros impares del 1 al 50


impares = [x for x in range (1,51) if x % 2 != 0]
print(impares)


# Calcular precio con descuento

precios_originales = [100,200,300,400]
precios_descuentos = [precio * 0.9 for precio in precios_originales]
print(precios_descuentos)







