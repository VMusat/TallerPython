# Estructura básica de una función
def suma(a, b=4):
    resultado = a + b
    return resultado


print(suma(3, 4))
print(suma(3))
print(suma(3, b=8))
print(suma(a=2, b=6))


# Esta función permite observar el desempaquetado de parámetros posicionales y de palabras clave
def imprimir_valores(*args, **kwargs):
    # Extraemos los parámetros posicionales
    for arg in args:
        print(arg)
    # Extraemos los parámetros de palabras clave
    for key, value in kwargs.items():
        print(f"{key}: {value}")


imprimir_valores(1, 2, 3, nombre="Juan", edad=25)


# Una función lambda es una función corta y simple
cuadrado = lambda x: x ** 2
print(cuadrado(5))  # Imprime 25


# La función factorial es un sencillo ejemplo de recursividad
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)


# Probemos la función con algunos valores
for i in range(6):
    print(f"{i}! = {factorial(i)}")


# La iteración n de Fibonacci suma n-1 y n-2 de la sucesión. Empezando en Fib(1)=0 y Fib(2)=1
# Aunque se puede resolver de manera recursiva, la solución iterativa de este problema es más eficiente, investigala ;-D
def fibonacci(n):
    if n <= 0:
        return "El número debe ser mayor que cero."
    elif n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)


# Probemos la función con algunos valores
for i in range(1, 11):
    print(f"Fibonacci({i}): {fibonacci(i)}")


# Se pueden obtener funciones de librerías (o clases) de Python mediante import
# Mediante la librería math se obtienen elementos matemáticos
import math
def calcular_area_circulo(radio):
    area = math.pi * radio**2
    return area


radio_circulo = 5
area_resultante = calcular_area_circulo(radio_circulo)
print(f"El área del círculo con radio {radio_circulo} es {area_resultante:.2f}")





