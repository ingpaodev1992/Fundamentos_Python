# **Clase 1: Estructuras Condicionales en Python** 🌟

Las estructuras condicionales nos permiten tomar decisiones en el código basado en ciertas condiciones. Por ejemplo, podríamos querer asistir a un lugar con una restricción de edad o aprobar una materia con una nota mínima. En Python, usamos las estructuras condicionales para estos casos.

## **1. La Estructura `if`** 🟢

La estructura `if` se utiliza para evaluar una condición. Si la condición se cumple (es verdadera), se ejecuta el bloque de código dentro de `if`.

### **Ejemplo básico**:

```python
x = 10

if x > 5:  # Condición
    print("x es mayor que 5")  # Acción si la condición es verdadera
```

En este caso, dado que `x` es 10, se imprime "x es mayor que 5".

---

## **2. Uso de `else` y `elif`** 🔄

Si queremos evaluar más condiciones, utilizamos `else` y `elif`.

- **`else`**: se ejecuta si la condición del `if` es falsa.
- **`elif`**: se usa para evaluar condiciones adicionales.

### **Ejemplo**:

```python
x = 3

if x > 5:
    print("x es mayor que 5")
elif x < 5:
    print("x es menor que 5")  # Esta línea se ejecutará
else:
    print("x es igual a 5")
```

En este caso, se imprimirá "x es menor que 5".

---

## **3. Combinación de Condiciones** 🤝

Podemos combinar múltiples condiciones usando `and`, `or` y `not`.

- **`and`**: ambas condiciones deben ser verdaderas.
- **`or`**: al menos una de las condiciones debe ser verdadera.
- **`not`**: invierte el valor de verdad de la condición.

### **Ejemplo con `and`**:

```python
x = 15
y = 20

if x > 10 and y > 15:
    print("Ambas condiciones son verdaderas")  # Se ejecuta
```

### **Ejemplo con `or`**:

```python
if x > 20 or y > 15:
    print("Al menos una condición es verdadera")  # Se ejecuta
```

### **Ejemplo con `not`**:

```python
if not (x > 20):
    print("x no es mayor que 20")  # Se ejecuta
```

---

## **4. Ejercicio Práctico**: Determinar Acceso a una Biblioteca 📚

### **Descripción**:

Vamos a crear un programa que determine si una persona tiene acceso a una biblioteca basado en su edad y si es miembro.

### **Código**:

```python
edad = 16  # Cambia este valor para probar diferentes edades
es_miembro = True  # Cambia a False para ver el otro caso

if es_miembro and edad >= 15:
    print("Tienes acceso a la biblioteca.")
elif not es_miembro and edad < 15:
    print("No tienes acceso ya que no eres miembro y tu edad es menor a 15.")
else:
    print("No tienes acceso ya que no eres miembro.")
```

### **Paso a Paso**:

1. Define la edad y si es miembro o no.
2. Evalúa si es miembro y su edad es mayor o igual a 15.
3. Si no es miembro y su edad es menor a 15, imprime un mensaje.
4. En caso contrario, indica que no tiene acceso.

---

## **5. Ejercicio Avanzado**: Piedra, Papel o Tijera ✊✋✌️

### **Descripción**:

Crea un juego simple de Piedra, Papel o Tijera entre dos jugadores.

### **Código**:

```python
jugador1 = input("Jugador 1, elige: piedra, papel o tijera: ")
jugador2 = input("Jugador 2, elige: piedra, papel o tijera: ")

if jugador1 == jugador2:
    print("Es un empate.")
elif (jugador1 == "piedra" and jugador2 == "tijera") or \
     (jugador1 == "papel" and jugador2 == "piedra") or \
     (jugador1 == "tijera" and jugador2 == "papel"):
    print("Jugador 1 gana!")
else:
    print("Jugador 2 gana!")
```

### **Paso a Paso**:

1. Solicita la elección de cada jugador.
2. Compara las elecciones.
3. Imprime el resultado basado en las reglas del juego.

---

## **Conclusión** 🏁

Las estructuras condicionales son una herramienta poderosa en Python que nos permite tomar decisiones lógicas. Con la práctica y la comprensión de los ejemplos proporcionados, puedes aplicar estos conceptos a diversas situaciones.

---
