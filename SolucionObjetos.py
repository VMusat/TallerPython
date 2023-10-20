class Animal:
    def __init__(self, nombre, tipo, edad):
        self.nombre = nombre
        self.tipo = tipo  # Carnivoro, Vegetariano, Omnivoro
        self.edad = edad
        self.salud = 100

    def hacer_sonido(self):
        pass

    def recibir_alimento(self, alimento):
        # Si el alimento es "carne" y el animal es de tipo "Carnivoro" u "Omnivoro", suma 10 a la vida que ya tenía
        # Si el aliemnto es "vegetales" y el animal es de tipo "Vegetariano" u "Omnivoro", suma 5 a la vida que ya tenia
        # En otro caso print(f"{self.nombre} No ha comido el alimento: {alimento}")
        pass


class Gato(Animal):

    # La clase gato tiene un atributo de clase llamado ratones_atrapados, iniciado en 0

    def __init__(self, nombre, edad):
        # El tipo de cualquier gato es "Omnivoro" y debe inicializarse como tal
        pass

    def hacer_sonido(self):
        return "Miau"

    def atrapar_raton(self):
        # Cuando atrapa un raton, el propio gato recibe el alimento "carne" y
        # suma 1 a los ratones_atrapados de la clase Gato
        pass


class Loro(Animal):
    def __init__(self, nombre, edad, palabras):
        # El tipo de cualquier loro es "Vegetariano" y debe inicializarse como tal
        # Los loros tienen un atributo de instancia con las palabras que se saben, es una lista de strings
        # La lista comineza con la palabra "Hola", y se añaden todas las recibidas por parámetro (que es una lista)
        # (El atributo de instancia tiene el nombre "palabras")
        pass

    def hacer_sonido(self):
        # Cuando los loros hacen sonidos, lo hacen con todas las palabras que saben
        # Devuelve un solo string con todas las palabras que sabe separadas por espacios
        # (Sustituye None)
        return None

    def nueva_palabra(self, palabra):
        # Añade una nueva palabra a la lista de palabras que sabe
        pass


class Serpiente(Animal):

    def __init__(self, nombre, edad, longitud):
        # El tipo de cualquier serpiente es "Carnivoro" y debe inicializarse como tal
        # Las serpientes tienen un atributo de instancia con su longitud en centimetros, es un entero
        # Esta longitud se recibe por parámetro
        # (El atributo de instancia tiene el nombre "longitud")
        pass

    def hacer_sonido(self):
        return "Pssssss"

    def recibir_alimento(self, alimento):
        # Cuando una serpiente recibe alimento, además de lo que le pasa a un animal normal,
        # también aumenta su longitud en 2cm si su longitud no supera ya los 50cm.
        # Si lo supera print(self.nombre + " ha comido demasiado y no crecerá más")
        pass


class Zoologico:
    def __init__(self):
        self.animales = {}

    def agregar_animal(self, animal):
        if isinstance(animal, Animal):
            self.animales[animal.nombre] = animal
            print(f"{animal.nombre} ha sido agregado al zoológico.")
        else:
            print("No se puede agregar un objeto que no es un Animal.")

    def alimentar_animales(self, alimento):
        for nombre, animal in self.animales.items():
            animal.recibir_alimento(alimento)

    def mostrar_informacion_general(self):
        print("\nInformación general del zoológico:")
        for nombre, animal in self.animales.items():
            print(f"{nombre} ({animal.tipo}), Edad: {animal.edad}, Salud: {animal.salud}")
        print("\n")

    def congregar_animales(self):
        for _, animal in self.animales.items():
            print(animal.hacer_sonido())
        print("\n")


# PARTE DE TEST
# Crear instancias de animales y agregarlos al zoológico
animal1 = Gato("Salem", 4)
animal2 = Gato("Bigotes", 6)
animal3 = Serpiente("Java", 2, 20)
animal4 = Serpiente("Boa", 5, 46)
animal5 = Loro("Carlos", 3, ["Galleta", "Guapo"])
animal6 = Loro("Pepe", 1, ["Premio"])

zoo = Zoologico()
zoo.agregar_animal(animal1)
zoo.agregar_animal(animal2)
zoo.agregar_animal(animal3)
zoo.agregar_animal(animal4)
zoo.agregar_animal(animal5)
zoo.agregar_animal(animal6)
zoo.mostrar_informacion_general()

print("PRUEBA 1")
print("Alimentamos los animales con carne")
zoo.alimentar_animales("carne")
zoo.mostrar_informacion_general()

print("PRUEBA 2")
print("Boa recibe un alimento carne (de un ratón que ha cazado). Medimos las serpientes")
zoo.animales["Boa"].recibir_alimento("carne")
print("La longitud de Boa es de " + str(zoo.animales["Boa"].longitud))
print("La longitud de Java es de " + str(zoo.animales["Java"].longitud))
print("Boa vuelve a cazar un ratón. Mostramos toda la información de los animales")
zoo.animales["Boa"].recibir_alimento("carne")
zoo.mostrar_informacion_general()

print("PRUEBA 3")
print("El cuidador se equivoca y pone chuches a los animales. Después los alimenta con vegetales")
zoo.alimentar_animales("chuches")
zoo.alimentar_animales("vegetales")
zoo.mostrar_informacion_general()

print("PRUEBA 4")
print("Salem y Bigotes salen a cazar ratones. Salem caza 2 y Bigotes 1")
zoo.animales["Salem"].atrapar_raton()
zoo.animales["Salem"].atrapar_raton()
zoo.animales["Bigotes"].atrapar_raton()
print("El total de ratones atrapados por los gatos es " + str(Gato.ratones_atrapados))
zoo.mostrar_informacion_general()

print("PRUEBA 5")
print("Carlos, ante tantos ratones, aprende una nueva palabra. Pepe aprende a mandarle callar")
zoo.animales["Carlos"].nueva_palabra("Ratones")
zoo.animales["Pepe"].nueva_palabra("Callate")
zoo.congregar_animales()
