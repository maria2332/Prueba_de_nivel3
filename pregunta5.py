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

    # Método para buscar un valor en el árbol
    def buscar(self, valor):
        if self.raiz is None:
            return None
        else:
            actual = self.raiz
            while actual is not None and actual.valor != valor:
                if valor < actual.valor:
                    actual = actual.izquierda
                else:
                    actual = actual.derecha
            return actual
        
    # Método para eliminar un valor del árbol
    def eliminar(self, valor):
        if self.raiz is None:
            return None
        else:
            actual = self.raiz
            padre = None
            while actual is not None and actual.valor != valor:
                padre = actual
                if valor < actual.valor:
                    actual = actual.izquierda
                else:
                    actual = actual.derecha
            if actual is None:
                return None
            elif padre is None:
                if actual.izquierda is None and actual.derecha is None:
                    self.raiz = None
                elif actual.izquierda is None:
                    self.raiz = actual.derecha
                elif actual.derecha is None:
                    self.raiz = actual.izquierda
                else:
                    reemplazo = self.__buscar_nodo_mas_izquierdo(actual.derecha)
                    self.eliminar(reemplazo.valor)
                    reemplazo.izquierda = actual.izquierda
                    reemplazo.derecha = actual.derecha
                    self.raiz = reemplazo
            elif actual.izquierda is None and actual.derecha is None:
                if padre.izquierda == actual:
                    padre.izquierda = None
                else:
                    padre.derecha = None
            elif actual.izquierda is None:
                if padre.izquierda == actual:
                    padre.izquierda = actual.derecha
                else:
                    padre.derecha = actual.derecha
            elif actual.derecha is None:
                if padre.izquierda == actual:
                    padre.izquierda = actual.izquierda
                else:
                    padre.derecha = actual.izquierda
            else:
                reemplazo = self.__buscar_nodo_mas_izquierdo(actual.derecha)
                self.eliminar(reemplazo.valor)
                reemplazo.izquierda = actual.izquierda
                reemplazo.derecha = actual.derecha
                if padre.izquierda == actual:
                    padre.izquierda = reemplazo
                else:
                    padre.derecha = reemplazo

    # Método para buscar el nodo más izquierdo de un subárbol
    def __buscar_nodo_mas_izquierdo(self, nodo):
        if nodo.izquierda is None:
            return nodo
        else:
            return self.__buscar_nodo_mas_izquierdo(nodo.izquierda)
        
    # Método para obtener la altura del árbol
    def altura(self, nodo):
        if nodo is None:
            return 0
        else:
            return max(self.altura(nodo.izquierda), self.altura(nodo.derecha)) + 1
        
    # Método para obtener el número de nodos del árbol
    def numero_nodos(self, nodo):
        if nodo is None:
            return 0
        else:
            return self.numero_nodos(nodo.izquierda) + self.numero_nodos(nodo.derecha) + 1
        
    # Método para obtener el número de nodos hoja del árbol
    def numero_nodos_hoja(self, nodo):
        if nodo is None:
            return 0
        elif nodo.izquierda is None and nodo.derecha is None:
            return 1
        else:
            return self.numero_nodos_hoja(nodo.izquierda) + self.numero_nodos_hoja(nodo.derecha)
        
    # Método para obtener el número de nodos con un solo hijo del árbol
    def numero_nodos_un_hijo(self, nodo):
        if nodo is None:
            return 0
        elif nodo.izquierda is None and nodo.derecha is None:
            return 0
        elif nodo.izquierda is None:
            return 1 + self.numero_nodos_un_hijo(nodo.derecha)
        elif nodo.derecha is None:
            return 1 + self.numero_nodos_un_hijo(nodo.izquierda)
        else:
            return self.numero_nodos_un_hijo(nodo.izquierda) + self.numero_nodos_un_hijo(nodo.derecha)
        
    # Método para obtener el número de nodos con dos hijos del árbol
    def numero_nodos_dos_hijos(self, nodo):
        if nodo is None:
            return 0
        elif nodo.izquierda is None and nodo.derecha is None:
            return 0
        elif nodo.izquierda is None:
            return self.numero_nodos_dos_hijos(nodo.derecha)
        elif nodo.derecha is None:
            return self.numero_nodos_dos_hijos(nodo.izquierda)
        else:
            return 1 + self.numero_nodos_dos_hijos(nodo.izquierda) + self.numero_nodos_dos_hijos(nodo.derecha)
        

