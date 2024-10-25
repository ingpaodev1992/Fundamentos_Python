# Clase 1: Apuntes sobre Listas en Python 📝🐍

## Introducción a las Listas 📋

Las listas en Python son estructuras de datos que permiten almacenar **colecciones de elementos**. Puedes imaginar las listas como cajas donde guardas distintos tipos de datos: números, cadenas de texto, o incluso otras listas. Son muy útiles cuando necesitas manejar múltiples valores relacionados en un solo lugar.

### Creación de una Lista 🚀

Para crear una lista, utilizamos corchetes `[]`, y los elementos se separan con comas.

```python
# Ejemplo básico
mi_lista = ["visitar la playa", "ir al museo", "cenar con amigos"]
print(mi_lista)
```

📌 **Nota**: Las listas pueden contener elementos de cualquier tipo, ya sea cadenas, números o incluso listas dentro de listas.

```python
# Lista con diferentes tipos de datos
mi_lista_mixta = [1, "hola", 3.14, True, [10, 20, 30]]
print(mi_lista_mixta)
```

## Operaciones Básicas con Listas 🛠️

### Acceder a Elementos de una Lista 🔍

Puedes acceder a los elementos de una lista usando **índices**. El índice de Python comienza en `0`, es decir, el primer elemento está en la posición `0`.

```python
# Acceder al primer elemento
primer_elemento = mi_lista[0]
print(primer_elemento)  # Output: visitar la playa
```

También puedes usar **índices negativos** para acceder a los elementos desde el final de la lista.

```python
# Acceder al último elemento
ultimo_elemento = mi_lista[-1]
print(ultimo_elemento)  # Output: cenar con amigos
```

### Slicing (Subconjuntos de Listas) ✂️

Puedes extraer partes de una lista utilizando el **slicing**, que te permite seleccionar un rango de elementos.

```python
# Obtener los primeros dos elementos
primeros_dos = mi_lista[0:2]
print(primeros_dos)  # Output: ['visitar la playa', 'ir al museo']

# Obtener desde el segundo elemento hasta el final
desde_segundo = mi_lista[1:]
print(desde_segundo)  # Output: ['ir al museo', 'cenar con amigos']
```

### Modificar Elementos de una Lista ✏️

Las listas son **mutables**, lo que significa que puedes cambiar sus elementos.

```python
# Cambiar el segundo elemento
mi_lista[1] = "visitar un parque"
print(mi_lista)  # Output: ['visitar la playa', 'visitar un parque', 'cenar con amigos']
```

### Añadir y Eliminar Elementos 🧩

- **Añadir elementos al final** con el método `.append()`.

```python
mi_lista.append("ir al cine")
print(mi_lista)  # Output: ['visitar la playa', 'visitar un parque', 'cenar con amigos', 'ir al cine']
```

- **Insertar elementos en una posición específica** con el método `.insert()`.

```python
mi_lista.insert(1, "comprar regalos")
print(mi_lista)  # Output: ['visitar la playa', 'comprar regalos', 'visitar un parque', 'cenar con amigos', 'ir al cine']
```

- **Eliminar elementos por su valor** con el método `.remove()`.

```python
mi_lista.remove("comprar regalos")
print(mi_lista)  # Output: ['visitar la playa', 'visitar un parque', 'cenar con amigos', 'ir al cine']
```

- **Eliminar elementos por su posición** usando `del` o el método `.pop()`.

```python
# Eliminar el último elemento
mi_lista.pop()
print(mi_lista)  # Output: ['visitar la playa', 'visitar un parque', 'cenar con amigos']

# Eliminar por índice
del mi_lista[0]
print(mi_lista)  # Output: ['visitar un parque', 'cenar con amigos']
```

### Funciones Útiles para Listas 🧮

- **len()**: Obtener la longitud de una lista (cuántos elementos tiene).

```python
print(len(mi_lista))  # Output: 2
```

- **max()** y **min()**: Funciones para encontrar el mayor y el menor valor en listas numéricas.

```python
numeros = [3, 1, 4, 2]
print(max(numeros))  # Output: 4
print(min(numeros))  # Output: 1
```

## Listas Dentro de Listas 🛌

Puedes almacenar listas dentro de otras listas para organizar mejor tus datos. Esto es útil cuando tienes datos agrupados.

```python
viajes = [["París", "Roma"], ["Nueva York", "Tokio"]]
print(viajes[0])  # Output: ['París', 'Roma']
print(viajes[0][1])  # Output: 'Roma'
```

## Ejercicios Prácticos 💪📚

### Ejercicio 1: Planificación de un Viaje 🏖️

Imagina que estás planificando un viaje. Crea una lista con los lugares que te gustaría visitar en un día y realiza las siguientes operaciones:

1. Añade un lugar más al final de la lista.
2. Elimina el primer lugar de la lista.
3. Imprime cuántos lugares quedan en tu lista.
4. Accede al último lugar de la lista sin saber cuántos elementos tiene.

**Solución:**

```python
# Paso 1: Crear la lista
itinerario = ["playa", "museo", "restaurante"]

# Paso 2: Añadir un lugar al final
itinerario.append("cine")

# Paso 3: Eliminar el primer lugar
del itinerario[0]

# Paso 4: Imprimir la cantidad de lugares restantes
print(len(itinerario))  # Output: 3

# Paso 5: Acceder al último lugar
print(itinerario[-1])  # Output: cine
```

### Ejercicio 2: Inventario de Mochila 🎒

Estás preparando tu mochila para una excursión. Crea una lista que contenga los artículos que vas a llevar. Haz lo siguiente:

1. Añade un artículo extra en la segunda posición.
2. Elimina el último artículo.
3. Encuentra la posición del artículo "agua".
4. Reemplaza el artículo "botella" por "termo".

**Solución:**

```python
# Paso 1: Crear la lista
mochila = ["botella", "comida", "ropa", "agua"]

# Paso 2: Añadir un artículo extra en la segunda posición
mochila.insert(1, "linterna")

# Paso 3: Eliminar el último artículo
mochila.pop()

# Paso 4: Encontrar la posición del artículo "agua"
print(mochila.index("agua"))  # Output: 3

# Paso 5: Reemplazar "botella" por "termo"
mochila[mochila.index("botella")] = "termo"
print(mochila)  # Output: ['termo', 'linterna', 'comida', 'agua']
```

### Ejercicio 3: Análisis de Datos con Listas 📊

Crea una lista con las temperaturas promedio de una semana y realiza los siguientes pasos:

1. Imprime la temperatura más alta y la más baja.
2. Elimina las temperaturas de los primeros dos días.
3. Calcula el promedio de las temperaturas restantes.

**Solución:**

```python
# Paso 1: Crear la lista
temperaturas = [22.5, 21.0, 23.5, 24.0, 22.8, 25.3, 23.0]

# Paso 2: Imprimir la temperatura más alta y la más baja
print(max(temperaturas))  # Output: 25.3
print(min(temperaturas))  # Output: 21.0

# Paso 3: Eliminar las temperaturas de los primeros dos días
del temperaturas[0:2]

# Paso 4: Calcular el promedio de las temperaturas restantes
promedio = sum(temperaturas) / len(temperaturas)
print(promedio)  # Output: 23.72
```

---

### Resumen Final 📑

Las listas en Python son poderosas herramientas para organizar y manipular datos de manera flexible. Con ellas puedes realizar desde operaciones básicas como añadir y eliminar elementos, hasta análisis más avanzados como ordenar y filtrar información. Practica utilizando listas en situaciones de la vida real, como la planificación de un viaje o el manejo de inventarios.

¡Sigue practicando y pronto dominarás las listas! 🔥
