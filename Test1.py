
entero = 34
flotante = 3.14
booleano = True
cadena = 'Hola123'

# Operaciones entre distintos tipos, prevalece el más "pesado"
prueba1 = entero+flotante
print(prueba1)
print(type(prueba1))
# Los booleanos son numerales en Python
prueba2 = entero+booleano
print(prueba2)
print(type(prueba2))
# Concatenación de cadenas
prueba3 = cadena+str(booleano)+str(flotante)
print(prueba3)
print(type(prueba3))

# Sirven para escribir los prints
parte1 = "variables"
parte2 = 3
print("Así se introducen "+parte1+" en los prints de Python "+str(parte2))

# También se pueden recoger datos introducidos por el usuario
respuesta = input("¿Qué nota le dais a esta introducción?")
print("La respuesta es "+respuesta)
# Se devuelven cadenas, hay que convertirlos en el tipo adecuado para operar
valor = 10-int(respuesta)
print("Para llegar al 10 me faltan "+str(valor)+" puntos")




