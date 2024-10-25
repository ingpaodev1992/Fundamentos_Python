import math

class CuerpoCeleste:

    # Constante de gravitación universal (en m³ kg⁻¹ s⁻²)

    constante_gravitacional = 6.67430e-11

    def __init__(self, nombre, masa, diametro):
        self.nombre = nombre
        self.masa = masa  # en kg
        self.diametro = diametro  # en km
        self.__edad = None  # Edad en millones de años (atributo privado para encapsulación)
    
    # Método para obtener información del cuerpo celeste

    def info(self):
        return f"{self.nombre}: Masa = {self.masa} kg, Diámetro = {self.diametro} km"

    # Método para calcular la gravedad en la superficie del cuerpo celeste

    def gravedad_superficie(self):
        radio = (self.diametro * 1000) / 2  # Convertimos km a m y obtenemos el radio
        gravedad = (self.constante_gravitacional * self.masa) / (radio ** 2)
        return f"Gravedad en superficie de {self.nombre}: {gravedad} m/s²"

    # Encapsulación: Métodos para obtener y establecer la edad (atributo privado)

    def get_edad(self):
        return self.__edad
    
    def set_edad(self, edad):
        if edad >= 0:
            self.__edad = edad
        else:
            print("La edad no puede ser negativa.")


# Creacion de clases derivadas

# Clase Planeta

class Planeta(CuerpoCeleste):
    def __init__(self, nombre, masa, diametro, distancia_sol):
        super().__init__(nombre, masa, diametro)
        self.distancia_sol = distancia_sol  # en millones de km
    
    def orbita(self):
        return f"{self.nombre} orbita alrededor del sol a una distancia de {self.distancia_sol} millones de km"

# Clase Estrella

class Estrella(CuerpoCeleste):
    def __init__(self, nombre, masa, diametro, temperatura_superficie):
        super().__init__(nombre, masa, diametro)
        self.temperatura_superficie = temperatura_superficie  # en grados Celsius
    
    def brillar(self):
        return f"{self.nombre} brilla con una temperatura de {self.temperatura_superficie} °C"

# Clase Luna

class Luna(CuerpoCeleste):
    def __init__(self, nombre, masa, diametro, planeta_orbita):
        super().__init__(nombre, masa, diametro)
        self.planeta_orbita = planeta_orbita
    
    def revolucionar(self):
        return f"{self.nombre} gira alrededor de {self.planeta_orbita}"


# Polimorfismo y funcion


# Función polimórfica para simular movimiento

def simular_movimiento(cuerpo):
    if isinstance(cuerpo, Planeta):
        print(cuerpo.orbita())
    elif isinstance(cuerpo, Estrella):
        print(cuerpo.brillar())
    elif isinstance(cuerpo, Luna):
        print(cuerpo.revolucionar())
    else:
        print(f"{cuerpo.nombre} no tiene movimiento definido")


# Creacion de objetos de cada clase para ver funcionalidad de todo

# Crear instancias de los cuerpos celestes

tierra = Planeta("Tierra", 5.972e24, 12742, 149.6)
sol = Estrella("Sol", 1.989e30, 1391016, 5500)
luna = Luna("Luna", 7.342e22, 3474, "Tierra")

# Llamar a los métodos y simular movimientos

print(tierra.info())
print(tierra.gravedad_superficie())
tierra.set_edad(4500)  # Edad en millones de años
print(f"Edad de la Tierra: {tierra.get_edad()} millones de años")

print(sol.info())
print(sol.gravedad_superficie())
sol.set_edad(4600)
print(f"Edad del Sol: {sol.get_edad()} millones de años")

print(luna.info())
print(luna.gravedad_superficie())
luna.set_edad(4000)
print(f"Edad de la Luna: {luna.get_edad()} millones de años")

# Simulación de movimiento (polimorfismo en acción)

simular_movimiento(tierra)
simular_movimiento(sol)
simular_movimiento(luna)
