import random

# Definimos la clase Nodo que representa cada nodo del árbol
class Nodo:
    def __init__(self, valor):
        self.valor = valor
        self.izquierda = None
        self.derecha = None

# Definimos la clase Arbol que representa el árbol binario de búsqueda
class Arbol:
    def __init__(self):
        self.raiz = None

    # Método para insertar un nuevo nodo en el árbol
    def insertar(self, valor):
        nuevo_nodo = Nodo(valor)
        if self.raiz is None:
            self.raiz = nuevo_nodo
        else:
            actual = self.raiz
            while True:
                if valor < actual.valor:
                    if actual.izquierda is None:
                        actual.izquierda = nuevo_nodo
                        break
                    else:
                        actual = actual.izquierda
                elif valor > actual.valor:
                    if actual.derecha is None:
                        actual.derecha = nuevo_nodo
                        break
                    else:
                        actual = actual.derecha

    # Método para realizar el barrido preorden del árbol
    def preorden(self, nodo):
        if nodo is not None:
            print(nodo.valor)
            self.preorden(nodo.izquierda)
            self.preorden(nodo.derecha)

    # Método para realizar el barrido inorden del árbol
    def inorden(self, nodo):
        if nodo is not None:
            self.inorden(nodo.izquierda)
            print(nodo.valor)
            self.inorden(nodo.derecha)

    # Método para realizar el barrido postorden del árbol
    def postorden(self, nodo):
        if nodo is not None:
            self.postorden(nodo.izquierda)
            self.postorden(nodo.derecha)
            print(nodo.valor)

