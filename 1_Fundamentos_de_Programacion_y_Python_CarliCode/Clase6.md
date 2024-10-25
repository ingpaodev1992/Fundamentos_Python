### 🎓 Clase 6: Operaciones Matemáticas en Python

En Python, las operaciones básicas como la **suma**, **resta**, **multiplicación** y **división** son fundamentales. Sin embargo, Python ofrece más operadores matemáticos avanzados que también son muy útiles. Vamos a explorarlos a continuación.

#### ✏️ Operaciones Básicas:
Primero, crearemos dos variables:
```python
a = 10
b = 3
```
Agregamos un comentario inicial:
```python
# Usando operadores matemáticos
```
Y ahora, imprimimos las operaciones básicas:
```python
print("➕ Suma:", a + b)
print("➖ Resta:", a - b)
print("✖️ Multiplicación:", a * b)
print("➗ División:", a / b)
```
Esto imprimirá el resultado de sumar, restar, multiplicar y dividir **10** y **3**. Es importante recordar que la multiplicación se representa con el asterisco `*`, y la división con la barra `/`.

#### 🔢 Operadores Avanzados:
Python también nos ofrece operadores más complejos como el **módulo**, la **división entera** y la **potenciación**. Vamos a verlos:

##### 🔄 Módulo:
El **módulo** (`%`) devuelve el residuo de una división.
```python
print("🔄 Módulo:", a % b)
```
Aquí, la salida sería **1**, porque el residuo de dividir 10 entre 3 es **1**.

##### 🔢 División Entera:
La **división entera** (`//`) devuelve la parte entera del cociente.
```python
print("📉 División Entera:", a // b)
```
En este caso, el resultado sería **3**, ya que es la parte entera de dividir 10 entre 3.

##### 💪 Potenciación:
La **potenciación** se realiza con dos asteriscos (`**`).
```python
print("💪 Potenciación:", a ** b)
```
Esto elevaría **10** a la potencia de **3**, resultando en **1000**.

#### ⚡ Atajos o Shorthands:
Cuando queremos modificar una variable y luego reasignarla, podemos utilizar operadores combinados:
```python
a += 2  # Suma 2 a 'a'
a -= 2  # Resta 2 a 'a'
a *= 2  # Multiplica 'a' por 2
a /= 2  # Divide 'a' entre 2
```
Estos atajos son más eficientes y claros en el código. ⚡

#### 📚 Precedencia de Operadores:
Cuando tenemos operaciones más complejas, Python sigue la **regla de precedencia** que podemos recordar con **PEMDAS** (Paréntesis, Exponentes, Multiplicación, División, Adición y Sustracción).

Por ejemplo:
```python
resultado = (2 + 3) * 4
print(resultado)
```
Aquí, se suman primero **2 + 3** (por estar entre paréntesis), y luego se multiplica por **4**. ✨

#### 🔍 Comparaciones y Operadores Booleanos:
Además de las operaciones matemáticas, Python ofrece operadores de comparación:
- `>` mayor que
- `<` menor que
- `>=` mayor o igual que
- `<=` menor o igual que
- `==` igual que
- `!=` diferente de

Ejemplo:
```python
print(a > b)  # True, porque 10 es mayor que 3
print(a < b)  # False, porque 10 no es menor que 3
print(a == b) # False, porque 10 no es igual a 3
```

Esto te permite comparar valores y obtener resultados booleanos (`True` o `False`). ✔️

---
