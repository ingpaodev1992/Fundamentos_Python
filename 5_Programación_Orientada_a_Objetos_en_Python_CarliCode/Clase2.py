# Ejercicio practico: Gestion de Biblioteca

# Crear una biblioteca

# Creacion Clases

# Definir la clase Libro

class Libro: 
    def __init__(self, titulo, autor):
        self.titulo = titulo
        self.autor = autor
        self.disponible = True

    def __str__(self):
        return f"{self.titulo} de {self.autor}"
    
#Definir la clase Persona

class Persona:
    def __init__(self, nombre):
        self.nombre = nombre
        self.libros_prestados = []

    def prestar_libro(self,libro):
        if libro.disponible:
            libro.disponible = False
            self.libros_prestados.append(libro)
            print(f"{self.nombre} ha prestado el libro '{libro.titulo}'.")
        else:
            print(f"El libro '{libro.titulo}' no esta disponible para prestamo")

    def retornar_libro(self,libro):
        if libro in self.libros_prestados:
            libro.disponible = True
            self.libros_prestados.remove(libro)
            print(f"{self.nombre} ha devuelto el libro '{libro.titulo}'.")
        else:
            print(f"{self.nombre} no tiene el libro '{libro.titulo}'para devolver")

# Definir la clase Biblioteca

class Biblioteca:
    def __init__(self):
        self.libros = []
        self.usuarios = []

    def añadir_libro(self, libro):
        self.libros.append(libro)
        print(f"Libro '{libro.titulo}' añadido a la biblioteca.")

    def registrar_usuario(self, usuario):
        self.usuarios.append(usuario)
        print(f"Usuario '{usuario.nombre}' registrado en la biblioteca.")

    def mostrar_libros_disponibles(self):
        disponibles = [libro for libro in self.libros if libro.disponible]
        if disponibles:
            print("Libros disponibles en la biblioteca:")
            for libro in disponibles:
                print(f"- {libro}")
        else:
            print("No hay libros disponibles en este momento.")


# Ejecución del ejercicio

# Crear libros
libro1 = Libro("El Principito", "Antoine de Saint-Exupéry")
libro2 = Libro("1984", "George Orwell")

# Crear usuarios
usuario1 = Persona("Paola Arguelles")

# Crear la biblioteca y añadir libros y usuarios

biblioteca = Biblioteca()
biblioteca.añadir_libro(libro1)
biblioteca.añadir_libro(libro2)
biblioteca.registrar_usuario(usuario1)

# Mostrar libros disponibles
biblioteca.mostrar_libros_disponibles()

# Prestar un libro
usuario1.prestar_libro(libro1)

# Mostrar libros disponibles después del préstamo
biblioteca.mostrar_libros_disponibles()

# Retornar el libro
usuario1.retornar_libro(libro1)

# Mostrar libros disponibles después de retornar
biblioteca.mostrar_libros_disponibles()


# Ejercicio Concesionaria de Vehiculos

# Clase Vehiculo
class Vehiculo:
    def __init__(self, marca, modelo, precio):
        self.marca = marca
        self.modelo = modelo
        self.precio = precio
        self.estado = True  # True indica que el vehículo está disponible

    def __str__(self):
        estado = "Disponible" if self.estado else "No disponible"
        return f"{self.marca} {self.modelo} - Precio: ${self.precio} - Estado: {estado}"


# Clase Persona
class Persona:
    def __init__(self, nombre):
        self.nombre = nombre
        self.vehiculos_comprados = []

    def comprar_vehiculo(self, vehiculo):
        if vehiculo.estado:  # Si el vehículo está disponible
            vehiculo.estado = False  # Marcar el vehículo como no disponible
            self.vehiculos_comprados.append(vehiculo)
            print(f"{self.nombre} ha comprado el vehículo {vehiculo.marca} {vehiculo.modelo}.")
        else:
            print(f"El vehículo {vehiculo.marca} {vehiculo.modelo} no está disponible para la compra.")


# Clase Concesionaria
class Concesionaria:
    def __init__(self):
        self.vehiculos = []
        self.usuarios = []

    def anadir_vehiculo(self, vehiculo):
        self.vehiculos.append(vehiculo)
        print(f"Vehículo {vehiculo.marca} {vehiculo.modelo} añadido a la concesionaria.")

    def registrar_usuario(self, usuario):
        self.usuarios.append(usuario)
        print(f"Usuario '{usuario.nombre}' registrado en la concesionaria.")

    def vehiculos_disponibles(self):
        disponibles = [vehiculo for vehiculo in self.vehiculos if vehiculo.estado]
        if disponibles:
            print("Vehículos disponibles para la compra:")
            for vehiculo in disponibles:
                print(f"- {vehiculo}")
        else:
            print("No hay vehículos disponibles en este momento.")

    def comprar_vehiculo(self, usuario, vehiculo):
        if usuario in self.usuarios:
            usuario.comprar_vehiculo(vehiculo)
        else:
            print("El usuario no está registrado en la concesionaria.")


# Crear vehículos
vehiculo1 = Vehiculo("Honda", "Civic", 24000)
vehiculo2 = Vehiculo("Ford", "Mustang", 30000)
vehiculo3 = Vehiculo("BMW", "Serie 3", 40000)

# Crear usuario
usuario1 = Persona("Paola Arguelles")

# Crear concesionaria y añadir vehículos
concesionaria = Concesionaria()
concesionaria.anadir_vehiculo(vehiculo1)
concesionaria.anadir_vehiculo(vehiculo2)
concesionaria.anadir_vehiculo(vehiculo3)

# Registrar usuario
concesionaria.registrar_usuario(usuario1)

# Mostrar vehículos disponibles
concesionaria.vehiculos_disponibles()

# Realizar compra de un vehículo
concesionaria.comprar_vehiculo(usuario1, vehiculo2)

# Mostrar vehículos disponibles después de la compra
concesionaria.vehiculos_disponibles()
