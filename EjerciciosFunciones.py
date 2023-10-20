# EJERCICIO 1
# La función es_palindromo recibe un parámetro string y devuelve un resultado booleano que indica
# si las letras del string forman un palindromo, ignorando las mayúsculas y espacios en blanco.
# (Sustituir pass por return y completar la función)
def es_palindromo(palabra):
    pass


# Código para probar la función
texto = "Anita lava la tina"
if es_palindromo(texto):
    print(f'"{texto}" es un palíndromo.')
else:
    print(f'"{texto}" no es un palíndromo.')


# EJERCICIO 2
# La función generar_primos_hasta recibe un número como parámetro y devuelve una lista con todos los números primos
# (sin contar el 1) hasta dicho número (sin incluirlo)
# (Sustituir pass por return y completar la función)
def generar_primos_hasta(n):
    pass


# Código para probar la función
limite = 20
lista_primos = generar_primos_hasta(limite)
print(f"Números primos hasta {limite}: {lista_primos}")


# EJERCICIO 3
# La función encontrar_max_min recibe como parámetro una lista de números y devuelve de ella,
# dos números, el máximo y el mínimo, respectivamente
# (Sustituir los None por los números)
def encontrar_max_min(lista):
    return None, None


# Código para probar la función
numeros = [3, 8, 1, 5, 12, 7]
maximo, minimo = encontrar_max_min(numeros)
print(f"Lista: {numeros}\nMáximo: {maximo}, Mínimo: {minimo}")
