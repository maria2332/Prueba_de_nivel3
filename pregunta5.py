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
    while actual.izquierdo is not None:
        actual = actual.izquierdo
    return actual

# Función para encontrar la altura de un árbol
def altura(raiz):
    if raiz is None:
        return 0
    altura_izq = altura(raiz.izquierdo)
    altura_der = altura(raiz.derecho)
    return 1 + max(altura_izq, altura_der)

# Función para contar la cantidad de ocurrencias de un valor en el árbol
def contar_ocurrencias(raiz, valor):
    if raiz is None:
        return 0
    elif raiz.valor == valor:
        return 1 + contar_ocurrencias(raiz.izquierdo, valor) + contar_ocurrencias(raiz.derecho, valor)
    elif valor < raiz.valor:
        return contar_ocurrencias(raiz.izquierdo, valor)
    else:
        return contar_ocurrencias(raiz.derecho, valor)

# Función para contar la cantidad de números pares e impares en el árbol
def contar_pares_impares(raiz, pares=0, impares=0):
    if raiz is None:
        return pares, impares
    elif raiz.valor % 2 == 0:
        pares += 1
    else:
        impares += 1
    pares, impares = contar_pares_impares(raiz.izquierdo, pares, impares)
    pares, impares = contar_pares_impares(raiz.derecho, pares, impares)
    return pares, impares

# Generar los 1000 números aleatorios y cargarlos en el árbol
arbol = None
for i in range(1000):
    num = random.randint(1, 1000)
    arbol = insertar(arbol, num)

# Realizar los distintos tipos de recorrido del árbol
print("Recorrido preorden:")
preorden(arbol)
print("\nRecorrido inorden:")
inorden(arbol)
print("\nRecorrido postorden:")
postorden(arbol)
print("\nRecorrido por nivel:")
por_nivel(arbol)

# Buscar si un valor está en el árbol
buscar_valor = 500
if buscar(arbol, buscar_valor):
    print("\nEl valor", buscar_valor, "está en el árbol.")
else:
    print("\nEl valor", buscar_valor, "no está en el árbol.")

# Eliminar tres valores del árbol
eliminar_valor_1 = 250
eliminar_valor_2 = 750
eliminar_valor_3 = 1000
arbol = eliminar(arbol, eliminar_valor_1)
arbol = eliminar(arbol, eliminar_valor_2)
arbol = eliminar(arbol, eliminar_valor_3)

# Calcular la altura de los subárboles izquierdo y derecho
altura_izq = altura(arbol.izquierdo)
altura_der = altura(arbol.derecho)
print("\nAltura del subárbol izquierdo:", altura_izq)
print("Altura del subárbol derecho:", altura_der)

# Contar la cantidad de ocurrencias de un valor en el árbol
ocurrencias_valor = 500
cantidad_ocurrencias = contar_ocurrencias(arbol, ocurrencias_valor)
print("\nEl valor", ocurrencias_valor, "aparece", cantidad_ocurrencias, "veces en el árbol.")

# Contar la cantidad de números pares e impares en el árbol
pares, impares = contar_pares_impares(arbol)
print("\nCantidad de números pares en el árbol:", pares)
print("Cantidad de números impares en el árbol:", impares)

