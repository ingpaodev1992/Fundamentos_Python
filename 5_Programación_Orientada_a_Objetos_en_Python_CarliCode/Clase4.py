# Clase base

class Vehículo:
    def __init__(self, marca, modelo, precio):
        self.marca = marca
        self.modelo = modelo
        self.precio = precio
        self.disponible = True

    def mostrar_info(self):
        return f"Marca: {self.marca}, Modelo: {self.modelo}, Precio: {self.precio}, Disponible: {self.disponible}"

# Clase derivada Bicicleta

class Bicicleta(Vehículo):
    def __init__(self, marca, modelo, precio):
        super().__init__(marca, modelo, precio)
  
    def en_marcha(self):
        return "La bicicleta está en marcha."

# Clase derivada Camión

class Camión(Vehículo):
    def __init__(self, marca, modelo, precio):
        super().__init__(marca, modelo, precio)
  
    def motor_en_marcha(self):
        return "El motor del camión está en marcha."

# Clase Comprador

class Comprador:
    def __init__(self, nombre):
        self.nombre = nombre
        self.vehículos = []

    def comprar_vehículo(self, vehículo):
        if vehículo.disponible:
            vehículo.disponible = False
            self.vehículos.append(vehículo)
            print(f"{self.nombre} ha comprado el {vehículo.marca}.")
        else:
            print("Lo siento, el vehículo no está disponible.")

# Clase Concesionaria

class Concesionaria:
    def __init__(self):
        self.inventario = []
        self.clientes = []

    def añadir_vehículo(self, vehículo):
        self.inventario.append(vehículo)
        print(f"{vehículo.marca} ha sido añadido al inventario.")

    def registrar_cliente(self, comprador):
        self.clientes.append(comprador)
        print(f"El cliente {comprador.nombre} ha sido registrado.")

    def mostrar_vehículos_disponibles(self):
        print("Vehículos disponibles:")
        for vehículo in self.inventario:
            if vehículo.disponible:
                print(vehículo.mostrar_info())

# Creación de la concesionaria

concesionaria = Concesionaria()

# Añadiendo vehículos

bicicleta1 = Bicicleta("Giant", "Escape 3", 500)
camión1 = Camión("Ford", "F-150", 30000)

concesionaria.añadir_vehículo(bicicleta1)
concesionaria.añadir_vehículo(camión1)

# Registrando un comprador

comprador1 = Comprador("Zeus")
concesionaria.registrar_cliente(comprador1)

# Mostrando vehículos disponibles

concesionaria.mostrar_vehículos_disponibles()

# Comprando un vehículo

comprador1.comprar_vehículo(bicicleta1)
concesionaria.mostrar_vehículos_disponibles()