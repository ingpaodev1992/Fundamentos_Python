# Diccionarios en Python

# Ejemplo

mi_diccionario = {
    1: "Paola",
    2: "Maria Pau",
    3: "Maria T"
}

# Propiedades Clave de los Diccionarios


# 1. Clave única: No pueden existir dos claves iguales en un diccionario.

# 2. Mutable: Puedes modificar sus valores y agregar o eliminar pares de clave-valor.

# 3. Ordenado (Python 3.7+): Los diccionarios mantienen el orden de inserción de los elementos.

# Operaciones comunes con diccionarios

# Crear un diccionario

persona = {
    "nombre": "Paola",
    "apellido": "Arguelles",
    "altura": 1.57,
    "edad": 31
}

print (persona)

# Acceder a elementos

print (persona["nombre"])

# Modificar un valor

persona["edad"] = 30
print (persona["edad"])

# Eliminar un elemento

del persona["edad"]
print (persona)

# Metodos utiles de Diccionarios

# keys() : Retorna todas las claves del diccionario.

claves = persona.keys()
print (claves)

# values() : Retorna todos los valores del diccionario.

valores = persona.values()
print (valores)

# items() : Retorna pares clave-valor en forma de tuplas.

pares = persona.items()
print (pares)

# Ejemplo de practica 1

agenda_contactos = {
    "Maria Paula":{
        "Nombre":"Maria Paula",
        "Apellido":"Echeverria",
        "Edad":"7",
        "Altura":"1.05"
    },
      "Maria Teresa":{
        "Nombre":"Maria Teresa",
        "Apellido":"Salazar",
        "Edad":"63",
        "Altura":"1.55"
    }
}

print (agenda_contactos["Maria Paula"])

# Gestion de productos en una tienda

productos = {
    "Producto1": {
        "nombre": "Esfero negro",
        "descripcion": "Esfero negro de gel",
        "precio": 3000},
    "Producto2": {
        "nombre": "Esfero rojo",
        "descripcion": "Esfero rojo de gel",
        "precio": 3000},
    "Producto3": {
        "nombre": "Esfero morado",
        "descripcion": "Esfero morado de gel",
        "precio": 3000},
    }

