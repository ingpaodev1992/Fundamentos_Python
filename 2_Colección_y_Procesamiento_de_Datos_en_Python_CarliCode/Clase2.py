#Copiar una lista en Python

a = [1,2,3,4,5]
b = a

print(b)
print(a)

# Verificar la referencia de memoria para determinar si dos listas apuntan al mismo espacio de memoria

print(id(a))
print(id(b))

# Uso de slice para copiar una lista sin compartir memoria

a = [1,2,3,4,5]
c = a[:]

print(id(a))
print(id(c))

# Modificar listas y efectos en la memoria


a = [1,2,3,4,5]
b = a
b.append(6) # Anadir un elemento a 'b'
print(a)
print(b)

# Pero si usamos slicing

a = [1,2,3,4,5]
c = a[:]
c.append(6)  # Anadir un elemento a 'c'
print (a)
print (c)



# Ejercicio de practica 1

Libros_originales = ["Don Quijote", "Cien anos de soledad", "La Odisea"]
Libros_referencia = Libros_originales
Libros_copia = Libros_originales[:]

Libros_originales.append("El Principito")

# Verificacion :

print("Libros originales:",Libros_originales)
print("Libros referencia:",Libros_referencia)
print("Libros copiados:",Libros_copia)


# Ejercicio de practica 2


Pizza_maragarita = ["jamon", "queso", "pina", "peperonni"]
Copia_pizza_margarita = Pizza_maragarita[:]
Pizza_maragarita.append("salami")

# Verificacion

print ("La nueva receta de Pizza Margarita es:", Pizza_maragarita)
print ("La receta original de Pizza Margarita es:", Copia_pizza_margarita)

