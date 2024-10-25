# La Estructura del If

x = 10

if x > 5:
    print("x es mayor que 5")

# Uso del else y elif

z = 5

if z > 5 :
    print("z es mayor que 5")
elif z < 5:
    print("z es menor que 5")
else:
    print("z es igual a 5")


# Adivina que personaje del juego de Spyro es: 

Personaje = "purpura"

if Personaje =="purpura":
    print ("Puede tratarse de Spyro")
elif Personaje == "purpura y vuela":
    print ("Hay posibilidad alta de que se trate de Spyro")
else:
    print("Se trata de otro personaje de Spyro")

# Combinacion de condiciones

# And

x = 2
y = 3

if x < 10 and y < 10 :
    print("Ambas condiciones son verdaderas")

# Or

if x < 10 or y < 10 :
    print("Ambas condiciones son verdaderas")

# not

if not (x > 10):
    print("x no es mayor que 10")


# Ejercicio Practico

edad = 18
es_miembro = True

if es_miembro and edad >=18:
    print("Tienes acceso a la biblioteca")
elif not es_miembro and edad <18:
    print("No tienes acceso a la biblioteca ya que no eres miembro y tu edad es menor a 18.")
else:
    print("No tienes acceso ya que no eres miembro")



# Piedra, papel o tijera


jugador1 = input("jugador 1, elige: piedra, papel o tijera:")
jugador2 = input("jugador 1, elige: piedra, papel o tijera:")

if jugador1 == jugador2:
    print("Empate")
elif (jugador1 == "piedra" and jugador2 == "tijera") or (jugador1 == "papel" and jugador2 == "piedra") or (jugador1 == "tijera" and jugador2 == "papel"):
    print("Jugador 1 gana")
else:
    print("Jugador 2 gana")

