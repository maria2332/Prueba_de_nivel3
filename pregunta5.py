import random

# Definir la estructura del nodo del árbol
class Nodo:
    def __init__(self, valor):
        self.valor = valor
        self.izquierdo = None
        self.derecho = None

# Función para crear un nuevo nodo
def crear_nodo(valor):
    nuevo = Nodo(valor)
    return nuevo

# Función para insertar un valor en el árbol
def insertar(raiz, valor):
    if raiz is None:
        raiz = crear_nodo(valor)
    elif valor < raiz.valor:
        raiz.izquierdo = insertar(raiz.izquierdo, valor)
    else:
        raiz.derecho = insertar(raiz.derecho, valor)
    return raiz

# Función para recorrer el árbol en preorden
def preorden(raiz):
    if raiz is not None:
        print(raiz.valor, end=" ")
        preorden(raiz.izquierdo)
        preorden(raiz.derecho)

# Función para recorrer el árbol en inorden
def inorden(raiz):
    if raiz is not None:
        inorden(raiz.izquierdo)
        print(raiz.valor, end=" ")
        inorden(raiz.derecho)

# Función para recorrer el árbol en postorden
def postorden(raiz):
    if raiz is not None:
        postorden(raiz.izquierdo)
        postorden(raiz.derecho)
        print(raiz.valor, end=" ")

# Función para recorrer el árbol por nivel
def por_nivel(raiz):
    if raiz is None:
        return
    cola = [raiz]
    while len(cola) > 0:
        nodo_actual = cola.pop(0)
        print(nodo_actual.valor, end=" ")
        if nodo_actual.izquierdo is not None:
            cola.append(nodo_actual.izquierdo)
        if nodo_actual.derecho is not None:
            cola.append(nodo_actual.derecho)

# Función para buscar un valor en el árbol
def buscar(raiz, valor):
    if raiz is None:
        return False
    elif raiz.valor == valor:
        return True
    elif valor < raiz.valor:
        return buscar(raiz.izquierdo, valor)
    else:
        return buscar(raiz.derecho, valor)

# Función para eliminar un valor del árbol
def eliminar(raiz, valor):
    if raiz is None:
        return raiz
    if valor < raiz.valor:
        raiz.izquierdo = eliminar(raiz.izquierdo, valor)
    elif valor > raiz.valor:
        raiz.derecho = eliminar(raiz.derecho, valor)
    else:
        if raiz.izquierdo is None:
            temp = raiz.derecho
            raiz = None
            return temp
        elif raiz.derecho is None:
            temp = raiz.izquierdo
            raiz = None
            return temp
        temp = minimo_valor(raiz.derecho)
        raiz.valor = temp.valor
        raiz.derecho = eliminar(raiz.derecho, temp.valor)
    return raiz

# Función para encontrar el mínimo valor en el árbol
def minimo_valor(raiz):
    actual = raiz
    while actual.izquierdo is
