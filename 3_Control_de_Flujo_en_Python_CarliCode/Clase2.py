# Bucles de iteracion

# Bucles For:

#for item in_colleection:

numeros = [0,2,4,6,8,10,12]
for numero in numeros:
    print(numero)

# Rango con range()

for i in range (0,10):
    print(i)


# Bucles While:

# While condition:

x = 0
while x < 5:
    print(x)
    x +=2

# Uso del break y continue:

# Break:

while True:
    x = int(input("Ingrese un numero:"))
    if x == 3:
        break


# Continue

for y in range (6):
    if y == 3:
        continue
    print(y)

# Ejercicios practicos

# Numeros pares

for num in range (1,21):
    if num % 2 == 0:
        print(num)

 # Contar hasta N

N = int(input("Ingrese un numero:"))
contador = 1
while contador <= N:
    print(contador)
    contador += 1

# Encontrar fruta

frutas = ["manzana", "naranja", "platano", "tomate"]
buscar = input("Que fruta desea buscar?")
encontrada = False

for fruta in frutas:
    if fruta == buscar:
        encontrada = True
        print(f"{buscar} encontrada")
        break
if not encontrada:
    print(f"{buscar} no encontrada")