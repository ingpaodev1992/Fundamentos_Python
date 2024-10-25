# Programacion orientada a objetos

# Creacion de Clases y Objetos:


class Persona:
    def __init__(self, nombre,apellido, fecha_nacimiento):
        self.nombre = nombre
        self.apellido = apellido
        self.fecha_nacimiento = fecha_nacimiento

    def saludar(self):
        print(f"Hola, mi nombre es {self.nombre} {self.apellido}.")

# Creacion de Objetos:

persona1 = Persona("Carli","Florida","15 de octubre de 1994")
persona1.saludar()
    
# Metodos en Clases

def saludar(self):
    print(f"Hola, mi nombre es {self.nombre}.")


# Ejemplo practico

# Creacion de las Clases

class CuentaBancaria:
    def __init__(self, titular, balance=0):
        self.titular = titular
        self.balance = balance
        self.activa = True

    def depositar(self, monto):
        if self.activa:
            self.balance += monto
            print(f"Se ha depositado {monto}. Saldo actual: {self.balance}.")
        else:
            print("La cuenta esta inactiva, no se puede depositar.")

    def retirar(self,monto):
        if self.activa:
            if monto <= self.balance:
                self.balance -= monto
                print(f"Se ha retirado {monto}, Saldo actual: {self.balance}.")
            else:
                print("La cuenta esta inactiva, no se puede depositar.")

    def desactivar(self):
        self.activa = False
        print("La cuenta ha sido desactivada.")

    def activar(self):
        self.activa = True
        print ("La cuenta ha sido activada")


# Creacion de Objetos

cuenta_ana = CuentaBancaria("Ana",500)
cuenta_ana.depositar(200) 
cuenta_ana.retirar(100)
cuenta_ana.desactivar()       
cuenta_ana.depositar(50)
cuenta_ana.activar()
cuenta_ana.depositar(50)


# Ejercicio practico


class vehiculo:
    def __init__(self, marca, modelo, ano):
        self.marca = marca
        self.modelo = modelo
        self.ano = ano

    def mostrar_info(self):
        print(f"Vehiculo: {self.marca} {self.modelo}, Ano: {self.ano}")


vehiculo1 = vehiculo("Toyota","Corola","2022")

vehiculo1.mostrar_info()
        


# Ejercicio de Sistema de Reserva de Pasajes


class Pasajero:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

class Vuelo:
    def __init__(self, destino, capacidad):
        self.destino = destino
        self.capacidad = capacidad
        self.pasajeros = []

    def agregar_pasajero(self, pasajero):
        if len(self.pasajeros) < self.capacidad:
            self.pasajeros.append(pasajero)
            print(f"Pasajero {pasajero.nombre} agregado al vuelo.")
        else:
            print("No hay más asientos disponibles.")

    def listar_pasajeros(self):
        print(f"Pasajeros en el vuelo a {self.destino}:")
        for p in self.pasajeros:
            print(f"- {p.nombre}")

# Crear un vuelo

vuelo1 = Vuelo("Madrid", 3)
vuelo1.agregar_pasajero(Pasajero("Carlos", 30))
vuelo1.agregar_pasajero(Pasajero("Ana", 28))
vuelo1.listar_pasajeros()
vuelo1.agregar_pasajero(Pasajero("Luis", 25))
vuelo1.agregar_pasajero(Pasajero("Sofía", 22)) 































