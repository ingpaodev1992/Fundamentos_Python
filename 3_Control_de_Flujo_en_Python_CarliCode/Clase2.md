
# **Clase 2: Control de Flujo en Python: Bucles de Iteración**

**Bucles For y While:** 🔄

- **Bucles For:** Se utilizan para iterar sobre una colección (como listas o tuplas). La sintaxis básica es:

  ```python
  for item in collection:
      # código a ejecutar
  ```
- **Bucles While:** Se ejecutan mientras se cumpla una condición específica. La sintaxis básica es:

  ```python
  while condition:
      # código a ejecutar
  ```

### **A. Bucles For** 🌀

- **Descripción:** Permiten recorrer una colección de elementos.
- **Ejemplo de Uso:**

  ```python
  numeros = [1, 2, 3, 4, 5, 6]
  for numero in numeros:
      print(numero)  # Imprime cada número de la lista
  ```
- **Rango con `range()`:** 📏

  ```python
  for i in range(0, 10):  # Imprime del 0 al 9
      print(i)
  ```

  - Si deseas iniciar desde un número diferente:

  ```python
  for i in range(3, 10):  # Imprime del 3 al 9
      print(i)
  ```

### **B. Bucles While** ⏳

- **Descripción:** Se ejecuta mientras una condición sea verdadera.
- **Ejemplo de Uso:**

  ```python
  x = 0
  while x < 5:
      print(x)
      x += 1  # Incrementa x en 1
  ```
- **Uso de `break` y `continue`:** ⚠️

  - **break:** Termina el bucle inmediatamente.

  ```python
  while True:
      x = int(input("Ingrese un número: "))
      if x == 3:
          break  # Sale del bucle si x es 3
  ```

  - **continue:** Salta a la siguiente iteración.

  ```python
  for y in range(6):
      if y == 3:
          continue  # Salta el número 3
      print(y)  # Imprime 0, 1, 2, 4, 5
  ```

---

### **3. Ejercicios Prácticos** 📝

### **Ejercicio 1: Números Pares** 🎉

**Descripción:** Escribe un programa que imprima todos los números pares del 1 al 20.

**Solución:**

```python
for num in range(1, 21):  # Itera del 1 al 20
    if num % 2 == 0:  # Verifica si el número es par
        print(num)  # Imprime el número par
```

### **Ejercicio 2: Contar Hasta N** 🔢

**Descripción:** Crea un programa que cuente de 1 hasta un número N proporcionado por el usuario.

**Solución:**

```python
N = int(input("Ingrese un número: "))  # Solicita un número al usuario
contador = 1
while contador <= N:  # Mientras el contador sea menor o igual a N
    print(contador)
    contador += 1  # Incrementa el contador
```

### **Ejercicio 3: Encontrar Fruta** 🍏

**Descripción:** Dado una lista de frutas, el programa debe buscar si una fruta específica está en la lista.

**Solución:**

```python
frutas = ["manzana", "naranja", "plátano", "tomate"]
buscar = input("¿Qué fruta desea buscar? ")  # Solicita fruta al usuario
encontrada = False

for fruta in frutas:
    if fruta == buscar:
        encontrada = True
        print(f"{buscar} encontrada!")  # Imprime si la fruta fue encontrada
        break

if not encontrada:
    print(f"{buscar} no encontrada.")  # Imprime si la fruta no está en la lista
```

---

### **4. Resumen Dinámico** 📚

### **Bucles en Python: Resumen Visual** 🌟

- **Bucles For:** ✅ Iteran sobre colecciones. ✅ Usar `range()` para números secuenciales.
- **Bucles While:** ✅ Ejecutan mientras se cumpla una condición. ✅ Usar `break` para salir, `continue` para saltar.

---
