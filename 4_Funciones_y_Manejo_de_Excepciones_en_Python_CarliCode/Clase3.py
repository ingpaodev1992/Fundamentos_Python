# Funciones Recursivas

# Calcular el Factorial

def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)
    
print(factorial(5))

# Serie de Fibonacci

def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)
print(fibonacci(6))


# Sumar numeros naturales

def sumatoria(n):
    if n ==0:
        return 0
    else:
        return n+sumatoria(n-1)
print(sumatoria(4))