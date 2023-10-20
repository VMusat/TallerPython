class Personaje:
    # Variable de clase
    contador_personajes = 0

    def __init__(self, nombre, salud, ataque):
        # Variables de instancia
        self.nombre = nombre
        self._salud = salud
        self._ataque = ataque
        Personaje.contador_personajes += 1

    def mostrar_estado(self):
        print(f"{self.nombre}: Salud={self._salud}, Ataque={self._ataque}")

    @property
    def salud(self):
        return self._salud

    @salud.setter
    def salud(self, value):
        self._salud = value


# Crear una instancia de la clase Personaje
jugador1 = Personaje("Héroe", 100, 20)

# Acceder a los atributos y llamar a un método
print(jugador1.nombre)
print(jugador1.salud)
# print(jugador1._ataque)
jugador1.salud += 25
jugador1.mostrar_estado()

# Acceder a una variable de clase
print(f"Personajes creados: {Personaje.contador_personajes}")


class Guerrero(Personaje):
    def __init__(self, nombre, salud, ataque, arma):
        super().__init__(nombre, salud, ataque)
        self.arma = arma

    def mostrar_arma(self):
        print(f"{self.nombre} tiene un arma: {self.arma}")


# Crear una instancia de la clase derivada Guerrero
guerrero1 = Guerrero("Conquistador", 120, 25, "Espada")
guerrero1.mostrar_estado()
guerrero1.mostrar_arma()

