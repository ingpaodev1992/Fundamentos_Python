# Operaciones de entrada y de salida en consola

# Solicitar nombre

nombre = input("Por favor ingresa tu nombre:")


# Mostrar en consola lo que el usuario ha digitado

print (nombre)


# Solicitar edad

edad = input("Por favor, ingresa tu nombre")
print (edad)


# Tipo de Datos

print (type(nombre)) # String
print (type(edad)) # String


# Conversion de Tipos de Datos

# Enteros (int)

edad = int (input("Por favor ingresa tu edad:"))
print(type(edad))  # Ahora si sera un numero entero


# Flotante/Decimal (float)

edad = float (input("Por favor ingresa tu edad:"))
print(type(edad))  # Ahora si sera un numero decimal


# Manejo de errores 

edad = int (input("Ingresa tu edad:")) # Si el usuario no digita un numero entero se generara un error

# Se puede utilizar una estructura de control como try para evitar que el programa se detenga:

try:
    edad = int (input("Ingresa tu edad:"))
except ValueError:
    print ("Error: Debes ingresar un numero entero.")