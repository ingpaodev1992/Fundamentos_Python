# Listas de mas dimensiones (Matrices)

matriz = [[1,2,3],[4,5,6],[7,8,9]]

# Accediendo a elementos especificos de la matriz

elemento = matriz[2][2]
print (elemento)

# Ejemplo practico: Manejo de datos en una matriz

ventas = [[100,200,150],[80,220,300],[90,250,120]]
ventas_miercoles_seccion2 = ventas [2][1]
print (ventas_miercoles_seccion2)


# Listas de mas dimensiones y sublistas anidadas

data = [[[1,2],[3,4]],[[5,6],[7,8]]]

numero = data[1][0][1]
print(numero)

# Tuplas: Datos Inmutables (No se pueden modificar)

# Definicion de Tupla

mi_tupla = (1,2,3,4,5)

#mi_tupla[0] = 10 , esto generara un error porque las tuplas son inmutables

# Ejemplo de practica 1

coordenadas = (10.1234, -75.1234)
print (f"Latitud:{coordenadas[0]}, Longitud:{coordenadas[1]}")


# Ejemplo de practica 2

ventas = [[100,200,150], [120,210,180],[90,220,160],[110,190,170]]

promedios = [sum(columna)/len(ventas) for columna in zip(*ventas)]
print (promedios)

# Ejemplo de practica 3

personas = [("Carlos",25,"Bogota"),("Maria",30,"Medellin"),("Pedro",22,"Cali")]

for personas in personas :
    nombre, edad, ciudad = personas
    print (f"{nombre} tiene {edad} anos y vive en {ciudad}.")