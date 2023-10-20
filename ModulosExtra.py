import os
import re
import numpy as np


# Ejemplo 1
directorio = "./"  # Directorio actual
archivos = os.listdir(directorio)

print("Archivos en el directorio actual:")
for archivo in archivos:
    print(archivo)


# Ejemplo 2
nuevo_directorio = "./nuevo_directorio"
os.makedirs(nuevo_directorio)
print(f"Directorio {nuevo_directorio} creado.")


# Ejemplo 3
patron_telefono = r"\d{3}-\d{3}-\d{4}"
numero = "123-456-7890"

if re.match(patron_telefono, numero):
    print(f"{numero} es un número de teléfono válido.")
else:
    print(f"{numero} no es un número de teléfono válido.")


# Ejemplo 4
texto = "Hoy es 25 de octubre y la temperatura es 23.5°C"
numeros = re.findall(r"\d+\.\d+|\d+", texto)

print("Números en el texto:")
for numero in numeros:
    print(numero)


# Ejemplo 5
datos = np.array([1, 2, 3, 4, 5])
media = np.mean(datos)
desviacion_estandar = np.std(datos)

print(f"Array NumPy: {datos}")
print(f"Media: {media}")
print(f"Desviación Estándar: {desviacion_estandar}")


# Ejemplo 6
matriz_a = np.array([[1, 2], [3, 4]])
matriz_b = np.array([[5, 6], [7, 8]])

suma_matrices = matriz_a + matriz_b
producto_matrices = np.dot(matriz_a, matriz_b)

print("Matriz A:")
print(matriz_a)

print("\nMatriz B:")
print(matriz_b)

print("\nSuma de Matrices:")
print(suma_matrices)

print("\nProducto de Matrices:")
print(producto_matrices)
