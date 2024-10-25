# Tipos de datos: Cadenas o Strings

name = '''Carli'''
print(name)

# Consultando el tipo de dato : usamos la funcion type () para conocer el tipo de dato.

print (type(name))


# Formas de definir Strings

# Con comillas dobles

cadena_doble = "Paola"

# Con comillas simples

cadena_simple = 'Paola'

# Con comillas triples

cadena_triple = """Paola"""


# Uso de comillas triples para multilineas

cadena_multilinea = """Hola,
Mundo"""
print (cadena_multilinea)

# Indexacion de Cadenas : Acceder a caracteres por indice

cadena = "Hola"
print (cadena[0]) # Output: H
print (cadena[1]) # Output: o

# Indexacion de Cadenas : Acceso a caracteres desde el final

print (cadena[-1]) # Output: a
print (cadena[-2]) # Output: l

# Operaciones con cadenas

nombre = "Maria Paula"
apellido = "Echeverria"
nombre_completo = nombre + " " + apellido
print (nombre_completo)  # Output: Maria Paula Echeverria

# Repeticion de cadenas

saludo = "Hola"
print (saludo * 3) # Output: Hola Hola Hola

# Consultar longitud de una cadena

print (len(nombre_completo)) # Output: 22

# Metodos de Cadenas 

# Convertir minusculas a mayusculas

name_1 = "Maria"
print (name_1.lower()) # Output: maria
print (name_1.upper()) # Output: MARIA

# Eliminar espacios en blanco

name_2 = "  Luis  "
print (name_2)

name_2 = "  Luis  "
print (name_2.strip())

# Uso de metodos y funciones

name_3 = "Paula"
print (name_3.lower()) # Metodo especifico para strings
print (len(name_3)) # Funcion general de Python