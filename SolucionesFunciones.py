# EJERCICIO 1
# Claro ejemplo del tipado de Python
# Las funciones lower() y replace() pertenecen al tipo (clase) string
# Aunque el parámetro de es_palindromo puede ser de cualquier tipo
# El iterprete durante la ejecución determina si es string y puede usar esas funciones
# Equivalente a usar Object en Java
def es_palindromo(palabra):
    palabra = palabra.lower().replace(" ", "")
    return palabra == palabra[::-1]


texto = "Anita lava la tina"
if es_palindromo(texto):
    print(f'"{texto}" es un palíndromo.')
else:
    print(f'"{texto}" no es un palíndromo.')


# EJERCICIO 2
# Es recomendable encapsular funciones repetitivas o con tareas bien definidas
def es_primo(numero):
    if numero < 2:
        return False
    for i in range(2, int(numero**0.5) + 1):
        if numero % i == 0:
            return False
    return True

def generar_primos_hasta(n):
    primos = [num for num in range(2, n) if es_primo(num)]
    return primos

limite = 20
lista_primos = generar_primos_hasta(limite)
print(f"Números primos hasta {limite}: {lista_primos}")


# EJERCICIO 3
def encontrar_max_min(lista):
    if not lista:
        return None, None
    maximo = max(lista)
    minimo = min(lista)
    return maximo, minimo

numeros = [3, 8, 1, 5, 12, 7]
maximo, minimo = encontrar_max_min(numeros)
print(f"Lista: {numeros}\nMáximo: {maximo}, Mínimo: {minimo}")
