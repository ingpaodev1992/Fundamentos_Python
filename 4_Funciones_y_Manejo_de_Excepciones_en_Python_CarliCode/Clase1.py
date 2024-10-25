# Funciones y manejo de excepciones

# Funciones

def nombre_funcion(parametros):
    pass

# Ejemplo de funcion 

def saludar():
    print("Hola Mundo")
saludar()


# Funciones con parametros

def saludar(nombre):
    print(f"Hola,{nombre}")
saludar("Paola")


# Parametros Predeterminados

def saludar(nombre="invitado"):
    print(f"Hola,{nombre}")

saludar()
saludar("Carli")


# Argumentos Posicionales y Nombrados

def saludar(nombre, apellido=""):
    print(f"Hola, {nombre} {apellido}")

saludar("Paola", "Arguelles")

saludar(apellido="Echeverria",nombre="Maria Paula")


# Manejo de Excepciones

# Calculadora


def sumar(a,b):
    return a+b


def restar(a,b):
    return a-b


def multiplicar(a,b):
    return a*b


def dividir(a,b):
    try:
        return a/b
    except ZeroDivisionError:
        return "Error, no se puede dividir por cero."
    

# Funcion Principal Calculadora


def calculadora():
    while True:
        print("Selecciona una operación:")
        print("1. Sumar")
        print("2. Restar")
        print("3. Multiplicar")
        print("4. Dividir")
        print("5. Salir")
        
        opcion = input("Ingrese su opción (1-5): ")

        if opcion == '5':
            print("Saliendo de la calculadora.")
            break

        if opcion in ['1', '2', '3', '4']:
            num1 = float(input("Ingrese el primer número: "))
            num2 = float(input("Ingrese el segundo número: "))

            if opcion == '1':
                print(f"La suma es: {sumar(num1, num2)}")
            elif opcion == '2':
                print(f"La resta es: {restar(num1, num2)}")
            elif opcion == '3':
                print(f"La multiplicación es: {multiplicar(num1, num2)}")
            elif opcion == '4':
                resultado = dividir(num1, num2)
                print(f"La división es: {resultado}")
        else:
            print("Opción no válida. Por favor intenta de nuevo.")

calculadora()


# Calculadora de IMC


def calcular_imc(peso, altura):
    return peso / (altura ** 2)

try:
    peso = float(input("Ingrese su peso en kg: "))
    altura = float(input("Ingrese su altura en metros: "))
    
    imc = calcular_imc(peso, altura)
    print(f"Su IMC es: {imc:.2f}")
except ValueError:
    print("Por favor, ingrese valores numéricos válidos.")
