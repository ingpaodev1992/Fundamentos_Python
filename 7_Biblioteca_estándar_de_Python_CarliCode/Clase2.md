# 🐍 Clase 2: Guía de Estudio: Bibliotecas `os`, `math` y `random` de Python

## 1. **Introducción a las Bibliotecas** 📚

Python ofrece varias bibliotecas estándar que permiten realizar tareas comunes sin necesidad de instalar paquetes adicionales. En esta clase, nos enfocaremos en:

- **`os`**: Interacción con el sistema operativo.
- **`math`**: Realización de cálculos matemáticos complejos.
- **`random`**: Generación de datos aleatorios.

---

## 2. **Biblioteca `os`** 🌍

La biblioteca `os` permite interactuar con el sistema operativo y manejar archivos y directorios.

### **Funciones Comunes:**

- **Obtener el directorio actual:**

```python
import os

directorio_actual = os.getcwd()
print(f"Directorio de trabajo actual: {directorio_actual}")
```

- **Listar archivos de un tipo específico:**

```python
archivos_txt = [f for f in os.listdir(directorio_actual) if f.endswith('.txt')]
print(f"Archivos .txt en el directorio: {archivos_txt}")
```

- **Renombrar archivos:**

```python
os.rename('caperucita.txt', 'cuento.txt')
print("Archivo renombrado a cuento.txt")
```

---

## 3. **Biblioteca `math`** 📐

La biblioteca `math` se utiliza para realizar operaciones matemáticas avanzadas, incluyendo el uso de constantes como π (pi).

### **Ejemplo de Cálculo de Área y Perímetro de un Círculo:**

```python
import math

radio = 5
area = math.pi * (radio ** 2)
perimetro = 2 * math.pi * radio

print(f"Área del círculo: {area}")
print(f"Perímetro del círculo: {perimetro}")
```

---

## 4. **Biblioteca `random`** 🎲

La biblioteca `random` se utiliza para generar números aleatorios y seleccionar elementos al azar.

### **Generación de Números Aleatorios:**

```python
import random

numero_aleatorio = random.randint(1, 10)
print(f"Número aleatorio entre 1 y 10: {numero_aleatorio}")
```

### **Seleccionar un Elemento Aleatorio de una Lista:**

```python
colores = ['rojo', 'azul', 'verde']
color_aleatorio = random.choice(colores)
print(f"Color aleatorio: {color_aleatorio}")
```

### **Barajar una Lista:**

```python
cartas = ['As', 'Rey', 'Reina', 'Jota', '10']
random.shuffle(cartas)
print(f"Cartas barajadas: {cartas}")
```

---

## 5. **Ejercicios Prácticos** 🚀

### **Ejercicio 1: Manejo de Archivos**

1. Crea un archivo de texto llamado `notas.txt` en tu directorio actual.
2. Usa la biblioteca `os` para listar todos los archivos de texto en el directorio.
3. Renombra `notas.txt` a `tareas.txt`.

### **Solución Paso a Paso:**

```python
import os

# Listar archivos .txt
archivos_txt = [f for f in os.listdir() if f.endswith('.txt')]
print(f"Archivos .txt en el directorio: {archivos_txt}")

# Renombrar el archivo
os.rename('notas.txt', 'tareas.txt')
print("Archivo renombrado a tareas.txt")
```

---

### **Ejercicio 2: Cálculos Matemáticos**

1. Escribe un programa que calcule el área y el perímetro de un círculo dado el radio.
2. Imprime los resultados con dos decimales.

### **Solución:**

```python
import math

radio = float(input("Ingrese el radio del círculo: "))
area = math.pi * (radio ** 2)
perimetro = 2 * math.pi * radio

print(f"Área del círculo: {area:.2f}")
print(f"Perímetro del círculo: {perimetro:.2f}")
```

---

### **Ejercicio 3: Generación Aleatoria**

1. Crea una lista con 5 frutas.
2. Selecciona y muestra una fruta aleatoria de la lista.
3. Baraja la lista de frutas y muestra el nuevo orden.

### **Solución:**

```python
import random

frutas = ['manzana', 'banana', 'naranja', 'fresa', 'kiwi']
fruta_aleatoria = random.choice(frutas)
print(f"Fruta aleatoria: {fruta_aleatoria}")

random.shuffle(frutas)
print(f"Frutas barajadas: {frutas}")
```

---

## 6. **Conclusión** 🎉

Las bibliotecas `os`, `math` y `random` son herramientas poderosas en Python que facilitan la manipulación de archivos, la realización de cálculos matemáticos y la generación de datos aleatorios.

### **Reflexión:**

Explora la documentación oficial para descubrir más funciones útiles en cada biblioteca. ¡Practica y experimenta con diferentes ejemplos! 💪
