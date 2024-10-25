# Herencia

class Vehículo:
    def __init__(self, marca, modelo, precio):
        self.marca = marca
        self.modelo = modelo
        self.precio = precio
        self.disponible = True  # Un atributo para indicar disponibilidad

    def vender(self):
        if self.disponible:
            self.disponible = False
            print(f"El {self.marca} ha sido vendido.")
        else:
            print(f"El {self.marca} no está disponible para la venta.")

    def esta_disponible(self):
        return self.disponible

    def obtener_precio(self):
        return self.precio

    def iniciar_funcionamiento(self):
        raise NotImplementedError("Este método debe ser implementado por la subclase.")

    def detener_funcionamiento(self):
        raise NotImplementedError("Este método debe ser implementado por la subclase.")
    
# Clases Hijas: Auto, Bicileta y Camion

# Clase Auto

class Auto(Vehículo):
    def iniciar_funcionamiento(self):
        if self.disponible:
            print(f"El motor del {self.marca} está en marcha.")
        else:
            print(f"El {self.marca} no está disponible para iniciar.")

    def detener_funcionamiento(self):
        if self.disponible:
            print(f"El motor del {self.marca} se ha detenido.")
        else:
            print(f"El {self.marca} no está disponible para detener.")

# Clase bicicleta

class Bicicleta(Vehículo):
    def iniciar_funcionamiento(self):
        if self.disponible:
            print(f"El motor de la bicicleta {self.marca} está en marcha.")
        else:
            print(f"La bicicleta {self.marca} no está disponible para iniciar.")

    def detener_funcionamiento(self):
        if self.disponible:
            print(f"El motor de la bicicleta {self.marca} se ha detenido.")
        else:
            print(f"La bicicleta {self.marca} no está disponible para detener.")

# Clase camion

class Camión(Vehículo):
    def iniciar_funcionamiento(self):
        if self.disponible:
            print(f"El motor del camión {self.marca} está en marcha.")
        else:
            print(f"El camión {self.marca} no está disponible para iniciar.")

    def detener_funcionamiento(self):
        if self.disponible:
            print(f"El motor del camión {self.marca} se ha detenido.")
        else:
            print(f"El camión {self.marca} no está disponible para detener.")

# Implementacion en la consecionaria

class Concesionaria:
    def __init__(self):
        self.inventario = []
        self.clientes = []

    def agregar_auto(self, auto):
        self.inventario.append(auto)

    def registrar_cliente(self, cliente):
        self.clientes.append(cliente)

    def mostrar_autos_disponibles(self):
        for auto in self.inventario:
            if auto.esta_disponible():
                print(f"{auto.marca} {auto.modelo} está disponible a ${auto.obtener_precio()}.")

    def vender_auto(self, cliente, auto):
        if auto.esta_disponible():
            auto.vender()
            print(f"{cliente} ha comprado el {auto.marca}.")
        else:
            print(f"Lo siento, {cliente}, el {auto.marca} no está disponible.")