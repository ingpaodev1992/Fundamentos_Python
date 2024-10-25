## Clase 5: Enteros, Flotantes y Booleanos 📚

### 1. **Enteros (`int`)** 🔢
- **Descripción**: Los enteros son números sin parte decimal. Pueden ser positivos, negativos o cero.
- **Ejemplo de Declaración**:
  ```python
  x = 10
  ```
- **Consultar el Tipo de Dato**:
  ```python
  print(type(x))  # Salida: <class 'int'>
  ```

### 2. **Números Flotantes (`float`)** 🌊
- **Descripción**: Los números flotantes representan valores con parte decimal. Se utilizan para representar números más precisos.
- **Ejemplo de Declaración**:
  ```python
  y = 5.0
  ```
- **Notación Científica**: Utilizada para números muy grandes o muy pequeños.
  ```python
  z = 1.2e6  # 1.2 * 10^6 = 1200000.0
  print(z)   # Salida: 1200000.0
  ```
  ```python
  a = 1.2e-6  # 1.2 * 10^-6 = 0.0000012
  print(a)    # Salida: 1.2e-06
  ```

### 3. **Operaciones Matemáticas** ➕➖✖️➗
- **Descripción**: Puedes realizar operaciones matemáticas básicas con enteros y flotantes. Los resultados de operaciones que involucran flotantes serán flotantes.

<div style="page-break-before: always;"></div>

- **Ejemplo de Código**:
  ```python
  result1 = x + y  # Suma de entero y flotante
  result2 = x + 10  # Suma de enteros
  result3 = y * 2  # Multiplicación de flotante y entero
  print("Resultados:", result1, result2, result3)
  ```

### 4. **Booleanos (`bool`)** ✅❌
- **Descripción**: Los booleanos tienen dos valores posibles: `True` (Verdadero) o `False` (Falso). Se utilizan para representar estados o condiciones.
- **Ejemplo de Declaración**:
  ```python
  is_true = True
  is_false = False
  ```
- **Consultar el Tipo de Dato**:
  ```python
  print(type(is_true))  # Salida: <class 'bool'>
  ```
<div style="page-break-before: always;"></div>

### **Ejemplos de Código Completo** 💻
Aquí tienes un ejemplo completo que muestra cómo trabajar con enteros, flotantes y booleanos:

```python
# Entero
x = 10
print("x:", x)
print("Tipo de x:", type(x))  # <class 'int'>

# Flotante
y = 5.0
print("y:", y)
print("Tipo de y:", type(y))  # <class 'float'>

# Notación científica
z = 1.2e6
print("z:", z)
a = 1.2e-6
print("a:", a)

# Operaciones matemáticas
result1 = x + y
result2 = x + 10
result3 = y * 2
print("Resultados:", result1, result2, result3)

# Booleanos
is_true = True
is_false = False
print("is_true:", is_true)
print("is_false:", is_false)
print("Tipo de is_true:", type(is_true))  # <class 'bool'>
```
