# Los condicionales en Python funcionan mediante el indentado
# Permiten comprobar lógica booleana
edad = 18
tiene_licencia = True
if edad >= 18 and tiene_licencia:
    print("Puede conducir legalmente.")
elif edad < 18:
    print("No puede conducir debido a su edad.")
else:
    print("No puede conducir porque no tiene licencia.")

# Permiten comprobar la pertenencia de elementos en colecciones
ingredientes = ["leche", "cacao", "azucar"]
if "sal" in ingredientes:
    print("No es salado")
elif "leche" in ingredientes and "cacao" in ingredientes:
    print("Puede ser Nocilla")
    if "avellanas" not in ingredientes:
        ingredientes.append("avellanas")
    else:
        print("Es Nocilla")
else:
    print("No se lo que es")

# Match permite simplificar la estructura if/elif/else
valor = 5
match valor:
    case 0:
        print("El valor es cero.")
    case 1 | 2 | 3:
        print("El valor está entre 1 y 3.")
    case _ if valor > 10:
        print("El valor es mayor que 10.")
    case _:
        print("El valor no coincide con ningún patrón específico.")

# El bucle while depende de contadores para cambiar las acciones de las iteraciones
contador = 0
while contador < 7:
    if contador == 2:
        print("Saltando la iteración cuando el contador es 2.")
        contador += 1
        continue
    print(f"Contador: {contador}")
    contador += 1
    if contador == 4:
        print("Terminando el bucle cuando el contador llega a 4.")
        break

# El bucle for permite iterar las colecciones con facilidad
frutas = ["manzana", "plátano", "uva"]
print("Iterando sobre una lista:")
for fruta in frutas:
    print(fruta)

# Permite iterar mediante índices utilizando range
print("\nIterando sobre un rango:")
numeros = [0, 1, 2, 3, 4, 5]
for i in range(2, 5):
    print(numeros[i])

# Else se ejecuta al final de un bucle si no se ha usado break
for i in range(5):
    if i > 4:
        break
    print(i)
else:
    print("El bucle for ha terminado sin interrupciones.")

# El bucle for permite iterar varias variables al mismo tiempo, por ejemplo en un diccionario:
diccionario = {"Jose": 35, "Pepe": 23.6, "Martin": 45}
for key, value in diccionario.items():
    if key == "Martin" or key == "Pepe":
        value += 30
        print("El dinero de " + key + " si le pagaramos 30 sería " + str(value))

# El bucle for también permite rellenar rapidamente una lista con elementos especificos
# Numeros divisibles entre 3 hasta el 30 incluido
divisibles = [num for num in range(3, 31) if num % 3 == 0]
print(divisibles)
