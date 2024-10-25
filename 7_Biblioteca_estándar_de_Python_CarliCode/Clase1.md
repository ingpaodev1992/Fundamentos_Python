# 📊 Clase 1: Guía de Estudio: Biblioteca `statistics` de Python y Análisis Estadístico

## 1. **Introducción al Análisis Estadístico** 📈

El análisis estadístico es fundamental para comprender el rendimiento de un negocio a través de los datos. Al analizar las ventas, se pueden identificar tendencias y patrones que informan decisiones estratégicas.

### **Conceptos Clave:**

- **Media:** Promedio de los datos.
- **Mediana:** Valor que divide el conjunto de datos en dos partes iguales.
- **Moda:** Valor que aparece con mayor frecuencia.
- **Desviación estándar:** Medida de la dispersión de los datos respecto a la media.
- **Varianza:** Promedio de las diferencias al cuadrado respecto a la media.
- **Rango:** Diferencia entre el valor máximo y mínimo.

## 2. **Uso de la Biblioteca `statistics`** 📚

La biblioteca `statistics` de Python proporciona funciones para calcular medidas estadísticas.

### **Importación de la Librería:**

```python
import statistics as stats
```

## 3. **Cálculo de Medidas Estadísticas** ⚙️

### **Ejemplo de Datos:**

Supongamos que tenemos datos de ventas mensuales en un archivo CSV.

### **Paso 1: Leer Datos desde un Archivo CSV**

```python
import csv

ventas = []
with open('ventas.csv', newline='') as csvfile:
    lector = csv.reader(csvfile)
    for fila in lector:
        ventas.append(float(fila[0]))  # Suponiendo que los datos están en la primera columna
```

### **Paso 2: Calcular la Media**

```python
media_ventas = stats.mean(ventas)
print(f"La media de las ventas es: {media_ventas}")
```

### **Paso 3: Calcular la Mediana**

```python
mediana_ventas = stats.median(ventas)
print(f"La mediana de las ventas es: {mediana_ventas}")
```

### **Paso 4: Calcular la Moda**

```python
moda_ventas = stats.mode(ventas)
print(f"La moda de las ventas es: {moda_ventas}")
```

### **Paso 5: Calcular la Desviación Estándar**

```python
desviacion_estandar = stats.stdev(ventas)
print(f"La desviación estándar es: {desviacion_estandar}")
```

### **Paso 6: Calcular la Varianza**

```python
varianza = stats.variance(ventas)
print(f"La varianza es: {varianza}")
```

### **Paso 7: Calcular el Rango**

```python
rango = max(ventas) - min(ventas)
print(f"El rango de las ventas es: {rango}")
```

## 4. **Ejercicios Prácticos** 🚀

### **Ejercicio 1: Análisis de Ventas**

1. Crea un archivo `ventas.csv` con datos de ventas mensuales (12 meses).
2. Escribe un script en Python que lea los datos y calcule la media, mediana, moda, desviación estándar y rango.

### **Solución Paso a Paso:**

```python
import csv
import statistics as stats

# Leer los datos desde el archivo CSV
ventas = []
with open('ventas.csv', newline='') as csvfile:
    lector = csv.reader(csvfile)
    for fila in lector:
        ventas.append(float(fila[0]))

# Calcular y mostrar medidas estadísticas
media_ventas = stats.mean(ventas)
mediana_ventas = stats.median(ventas)
moda_ventas = stats.mode(ventas)
desviacion_estandar = stats.stdev(ventas)
rango = max(ventas) - min(ventas)

print(f"La media de las ventas es: {media_ventas}")
print(f"La mediana de las ventas es: {mediana_ventas}")
print(f"La moda de las ventas es: {moda_ventas}")
print(f"La desviación estándar es: {desviacion_estandar}")
print(f"El rango de las ventas es: {rango}")
```

---

### **Ejercicio 2: Análisis de Tendencias**

1. Analiza los resultados obtenidos y determina qué medidas son más útiles en diferentes situaciones.
2. Comenta sobre qué información proporciona cada medida sobre el comportamiento de las ventas.

### **Solución:**

- **Media:** Útil para tener un valor promedio de ventas.
- **Mediana:** Muestra el punto medio y es resistente a valores extremos.
- **Moda:** Indica el producto más vendido.
- **Desviación estándar:** Indica cuánto varían las ventas respecto a la media.
- **Rango:** Muestra la diferencia entre el mejor y el peor mes de ventas.

## 5. **Conclusión** 🎉

El análisis estadístico es esencial para la toma de decisiones informadas en los negocios. Utilizar la biblioteca `statistics` de Python facilita este proceso y permite obtener insights valiosos de los datos.

### **Preguntas para Reflexionar:**

- ¿Por qué es importante calcular la media y la mediana?
- ¿Cómo afectan los valores atípicos a la media?

Recuerda, la práctica constante te ayudará a dominar estas herramientas. ¡Sigue explorando y experimentando! 💪
