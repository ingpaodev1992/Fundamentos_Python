# Manejo de Excepciones

# Division por cero

while True:
    try:
        divisor = int(input("Ingresa un numero divisor:"))
        resultado = 100 / divisor
        print(f"El resultado es: {resultado}")
        break
    except ZeroDivisionError:
        print("Error: El divisor no puede ser cero, Intenta de nuevo")
    except ValueError:
        print("Error: Debes introducir un numero entero")


# Manejo de multiples excepciones

while True:
    try:
        divisor = int (input("Ingresa un numero divisor:"))
        resultado = 100 / divisor
        print (f"El resultado es: {resultado}")
        break
    except (ZeroDivisionError, ValueError) as e:
        print(f"Error: {e}. Intenta de nuevo.")

# Ejercicios de practica

# Ingreso de Edad

while True:
    try:
        edad = int(input("Ingresa tu edad:"))
        print(f"Tienes {edad} anos.")
        break
    except ValueError:
        print("Error Debes introducir un numero entero")


# Calculo de Promedio 

calificaciones = []
while True:
    entrada = input("ingresa una calificacion(o 'fin' para terminar):")
    if entrada.lower() == 'fin':
        break
    try:
        calificacion = float(entrada)
        calificaciones.append(calificacion)
    except ValueError:
        print("Error: Debes introducir un numero.")
if calificaciones:
    promedio = sum(calificaciones) / len(calificaciones)
    print(f"El promedio es : {promedio}")
else:
    print("No se ingresaron calificaciones")