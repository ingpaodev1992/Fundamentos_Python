# 📚 Clase 2: **Gestión de Biblioteca con Programación Orientada a Objetos (POO)**

En esta clase, exploramos la implementación de una biblioteca utilizando POO. Se definieron tres clases principales: **Libro**, **Persona** y **Biblioteca**.

## 🏷️ **Clases y Atributos**

### 1. **Clase Libro 📖**

- **Constructor:**
  - **Atributos:**
    - `titulo`: El título del libro.
    - `autor`: El autor del libro.
    - `estado`: Indica si el libro está disponible para préstamo (disponible/no disponible).
- **Métodos:**
  - `prestar()`: Cambia el estado del libro a no disponible si está disponible.
  - `retornar()`: Cambia el estado del libro a disponible.

### 2. **Clase Persona 👤**

- **Constructor:**
  - **Atributos:**
    - `nombre`: El nombre de la persona.
    - `libros_prestados`: Lista de libros que la persona ha tomado prestados.
- **Métodos:**
  - `prestar_libro(libro)`: Permite a la persona prestar un libro si está disponible.
  - `retornar_libro(libro)`: Permite a la persona retornar un libro prestado.

### 3. **Clase Biblioteca 🏛️**

- **Constructor:**
  - **Atributos:**
    - `libros`: Colección de libros en la biblioteca.
    - `usuarios`: Colección de usuarios registrados.
- **Métodos:**
  - `añadir_libro(libro)`: Añade un libro a la colección de la biblioteca.
  - `registrar_usuario(usuario)`: Registra un nuevo usuario en la biblioteca.
  - `mostrar_libros_disponibles()`: Muestra los libros que están disponibles para préstamo.

---

## 🔍 **Ejercicio Práctico: Gestión de Biblioteca**

### 🚀 **Ejercicio 1: Crear una Biblioteca**

1. **Definir los libros**:

   ```python
   libro1 = Libro("El Principito", "Antoine de Saint-Exupéry")
   libro2 = Libro("1984", "George Orwell")
   ```
2. **Crear usuarios**:

   ```python
   usuario1 = Persona("Lady Di")
   ```
3. **Crear la biblioteca y añadir libros y usuarios**:

   ```python
   biblioteca = Biblioteca()
   biblioteca.añadir_libro(libro1)
   biblioteca.añadir_libro(libro2)
   biblioteca.registrar_usuario(usuario1)
   ```
4. **Mostrar libros disponibles**:

   ```python
   biblioteca.mostrar_libros_disponibles()
   ```

### 🚀 **Ejercicio 2: Prestar y Retornar Libros**

1. **Prestar un libro**:

   ```python
   usuario1.prestar_libro(libro1)
   ```
2. **Mostrar libros disponibles después del préstamo**:

   ```python
   biblioteca.mostrar_libros_disponibles()
   ```
3. **Retornar el libro**:

   ```python
   usuario1.retornar_libro(libro1)
   ```
4. **Mostrar libros disponibles después de retornar**:

   ```python
   biblioteca.mostrar_libros_disponibles()
   ```

---

## 💡 **Reto Final: Concesionaria de Vehículos 🚗**

**Descripción:** Implementar un sistema para gestionar la compra y venta de vehículos, donde un usuario pueda preguntar por los vehículos disponibles y sus precios, y también comprar uno.

### **Pasos a seguir**:

1. Crear una clase `Vehiculo` con atributos como `marca`, `modelo`, `precio`, y `estado` (disponible/no disponible).
2. Crear una clase `Concesionaria` que gestione una colección de vehículos y usuarios.
3. Implementar métodos para añadir vehículos, registrar usuarios, mostrar vehículos disponibles y realizar compras.

---
