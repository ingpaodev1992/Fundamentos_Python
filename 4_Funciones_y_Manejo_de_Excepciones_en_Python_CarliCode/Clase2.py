# Funciones Lambda y programacion funcional

# Ejemplo basico

suma = lambda x, y: x+y
resultado = suma(10,5)
print(resultado)

# Lista de numeros del 0 al 10

numeros = list(range(11))

cuadrados = list(map(lambda x: x**2, numeros))
print("Cuadrados:", cuadrados)

# Filtrado de Elementos en una lista

pares = list(filter(lambda x: x%2 ==0,numeros))
print("Numeros pares:",pares)


# Ejercicio de practica

# Sumar numeros

suma = lambda x, y: x+y

num1 = float(input("Ingresa el primer numero:"))
num2 = float(input("Ingresa el segundo numero:"))

resultado = suma(num1,num2)
print(f"La suma de {num1} y {num2} es : {resultado}")

# Cuadrados de Numeros

numeros = list(range(21))

cuadrados = list(map(lambda x: x**2, numeros))
print("Cuadrados:", cuadrados)


# Filtrar numeros Impares

numeros = list(range(21))

impares = list(filter(lambda x: x%2 !=0, numeros))
print("Numeros Impares:", impares)