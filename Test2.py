# La lista es la colección de elementos más básica en Python
# Es equivalente a los arrays en otros lenguajes de programación
lista = [6, 2, 1, 4, 6, 3, 1]
# Se puede acceder a sus elementos por su índice, al ser ordenada
elem1 = lista[0]
# Los índices negativos comienzan desde el final de la lista
elem2 = lista[-1]
print("Primer elemento: " + str(elem1) + ". Último elemento: " + str(elem2))

# Se pueden añadir y eliminar elementos de una lista, al ser modificable
lista.append(8)
lista.remove(elem1)
print("La lista tras añadir un elemento y eliminar el primero: " + str(lista))

# Se puede contar el número de elementos en total y de un elemento en concreto
# Admite elementos duplicados
cuenta1 = lista.count(elem2)
cuenta2 = len(lista)
print("Hay " + str(cuenta1) + " elementos 1 y " + str(cuenta2) + " elementos en total")

# Se pueden eliminar, insertar y modificar elementos de índices concretos
lista.pop(2)
lista.sort()
lista.insert(3, 33)
lista[0] = 9
print("¿Pudiste predecir como quedó la lista?: " + str(lista))

# Otra propiedad de las listas es el uso de slicing para recorrerlas
# El formato es [start:stop:step], siendo start (inclusive) y stop (excluyente) los indices
# Por ejemplo, para obtener cada segundo elemento de la siguiente lista (empezando en 2 y terminando en 8)
lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(lista[1:9:2])
# También se suele usar para obtener una lista (o cadena) invertida
cadena = "Python es genial"
print(cadena[::-1])


# Una tupla no puede ser modificada una vez creada
tupla = (2, 1, 9, True, "Reset")
# # tupla[3] = 2
print("El tercer elemento de la tupla es: "+str(tupla[3]))


# Un set es no ordenado, los elementos pueden aparecer en cualquier orden
# Sus elementos no pueden ser seleccionados por su índice
set_1 = {3, 6, "NotANumber", False, -1}
print("El set se representa como: "+ str(set_1))

# Un set no permite modificar sus elementos, pero sí añadir y elimiar
# No admite elementos duplicados
# La función pop elimina arbitrariamente un elemento
set_1.add(3)
set_1.add("New")
set_1.remove("NotANumber")
eliminado = set_1.pop()
print("El set queda: "+str(set_1)+". El elemento eliminado es: "+str(eliminado))


# Los diccionarios son una de las colecciones más útiles de Python
# Relaciona un elemento llamado clave con otro llamado valor
# Son ordenados y modificables, pero no funcionan por índices, sino por claves
# No admite claves duplicadas
diccionario = {"Id": 34, "Nombre": "Gato de  Schrodinger", "Vivo": True, "Vivo": False, 2: "Dos"}
print("El diccionario queda: "+str(diccionario))

# El acceso y modificación de elementos se realiza por claves
print(diccionario[2])
diccionario["Id"] = 56
diccionario["Edad"] = 8
print(diccionario.items())

# lista = [6, 2, 1, 4, 6, 3, 1]
# lista_mixta = [2, 4.65, "Numero", True, 4 == 2]
# matriz = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
#
# tupla = (2, 1, 9, True, "Reset")
# set_1 = {3, 6, "NotANumber", False, -1}
# diccionario = {"Id": 34, "Nombre": "Roberto", "Vivo": True, "Vivo": False}

