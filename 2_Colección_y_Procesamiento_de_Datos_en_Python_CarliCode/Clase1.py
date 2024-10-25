# Creacion de una Lista

mi_lista = ["origami", "cine","ir a la playa", "armar rompecabezas"]
print (mi_lista)

mi_lista_mixta = [1, "hola", 3.14, True, [10,20,30]]
print (mi_lista_mixta)

# Operaciones Basicas con Listas

# Acceder a elementos de una lista

primer_elemento = mi_lista[0]
print (primer_elemento)

ultimo_elemento = mi_lista[-1]
print (ultimo_elemento)

# Slicing (Subconjuntos de Listas)

# Obetener los primeros dos elementos

primero_dos = mi_lista[0:2]
print (primero_dos)

# Obtener desde el segundo elemento hasta el final

desde_segundo = mi_lista[1:]
print (desde_segundo)

# Modificar elementos de una lista

mi_lista[1] = "montar bicicleta"
print (mi_lista)


# Anadir y eliminar elementos

# Anadir elementos al final

mi_lista.append("ir al gym")
print (mi_lista)

# Insertar elementos en una posicion especifica

mi_lista.insert(1,"ir a piscina")
print (mi_lista)

# Elminar elementos por su valor

mi_lista.remove ("montar bicicleta")
print (mi_lista)

# Elminar elementos por su posicion

# Eliminar el utlimo elemento

mi_lista.pop()
print (mi_lista)

# Elminar por indice

del mi_lista[0]
print (mi_lista)


# Funciones utiles para Listas

# len()

print (len(mi_lista))

# max() y min()

numeros = [3,1,4,2]
print (max(numeros))
print (min(numeros))


# Listas dentro de listas: Datos agrupados

cursos = [["Excel", "Estadistica","Python"],["JavaScript", "Wordpress", "Angular"]]
print (cursos[0])
print (cursos[1])
print (cursos[0][1])
print (cursos[1][1])


# Ejercicio de practica 1

lugares_destino = ["Paris", "Turquia" , "Egipto", "Suiza"]
lugares_destino.append("Dubai")
print (lugares_destino)
del lugares_destino[0]
ultimo_lugar = lugares_destino[-1]
print (ultimo_lugar)


#  Ejercicio de practica 2

articulos_mochila = ["carpa","linterna","cobija", "encendedor"]
articulos_mochila.insert(1,"sleeping")
print (articulos_mochila)
articulos_mochila.pop()
print (articulos_mochila)
print (articulos_mochila.index("cobija"))
articulos_mochila[articulos_mochila.index("carpa")] = "fosforos"
print (articulos_mochila)

#  Ejercicio de practica 3

temperaturas = [23.2,24.5,27.8,28.9]
del temperaturas[0:2]
print(temperaturas)

promedio = sum(temperaturas)/len(temperaturas)
print(promedio)
