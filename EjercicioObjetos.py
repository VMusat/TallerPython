class Animal:
    def __init__(self, nombre, tipo, edad):
        self.nombre = nombre
        self.tipo = tipo
        self.edad = edad
        self.salud = 100

    def hacer_sonido(self):
        pass

    def recibir_alimento(self, alimento):
        if alimento == "carne" and (self.tipo == "Carnivoro" or self.tipo == "Omnivoro"):
            self.salud += 10
        elif alimento == "vegetales" and (self.tipo == "Vegetariano" or self.tipo == "Omnivoro"):
            self.salud += 5
        else:
            print(f"{self.nombre} No ha comido el alimento: {alimento}")


class Gato(Animal):
    ratones_atrapados = 0

    def __init__(self, nombre, edad):
        tipo = "Omnivoro"
        super().__init__(nombre, tipo, edad)

    def hacer_sonido(self):
        return "Miau"

    def atrapar_raton(self):
        self.recibir_alimento("carne")
        Gato.ratones_atrapados += 1


class Loro(Animal):
    def __init__(self, nombre, edad, palabras):
        tipo = "Vegetariano"
        super().__init__(nombre, tipo, edad)
        self.palabras = ["Hola"]
        for palabra in palabras:
            self.palabras.append(palabra)

    def hacer_sonido(self):
        oracion = ""
        for palabra in self.palabras:
            oracion = oracion + " " + palabra
        return oracion.lstrip()

    def nueva_palabra(self, palabra):
        self.palabras.append(palabra)


class Serpiente(Animal):

    def __init__(self, nombre, edad, longitud):
        tipo = "Carnivoro"
        super().__init__(nombre, tipo, edad)
        self.longitud = longitud

    def hacer_sonido(self):
        return "Pssssss"

    def recibir_alimento(self, alimento):
        Animal.recibir_alimento(self, alimento)
        if self.longitud < 50:
            self.longitud += 2
        else:
            print(self.nombre + " ha comido demasiado y no crecerá más")


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


