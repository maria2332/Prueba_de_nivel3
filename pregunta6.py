class Carta:
    def __init__(self, numero, palo):
        self.numero = numero
        self.palo = palo

    def __str__(self):
        return str(self.numero) + " de " + self.palo

import random

class Pila:
    def __init__(self, cartas=[], palo=None):
        self.cartas = cartas
        self.palo = palo

    def generar_aleatoria(self):
        self.cartas = []
        for palo in ["espada", "basto", "copa", "oro"]:
            for numero in range(1, 13):
                carta = Carta(numero, palo)
                self.cartas.append(carta)
        random.shuffle(self.cartas)

    def separar_por_palo(self):
        self.cartas_por_palo = {"espada": [], "basto": [], "copa": [], "oro": []}
        for carta in self.cartas:
            self.cartas_por_palo[carta.palo].append(carta)
        self.cartas = None

    def ordenar_por_numero(self):
        self.cartas.sort(key=lambda carta: carta.numero)

# Generar una pila aleatoria y separarla por palo
pila = Pila()
pila.generar_aleatoria()
pila.separar_por_palo()

# Ordenar la pila de espadas por número de carta
pila_espadas = Pila(cartas=pila.cartas_por_palo["espada"], palo="espada")
pila_espadas.ordenar_por_numero()