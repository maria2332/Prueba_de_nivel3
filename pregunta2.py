class Pedido:
    def __init__(self, nombre, multiverso, descripcion):
        self.nombre = nombre
        self.multiverso = multiverso
        self.descripcion = descripcion
        
    def determinar_prioridad(self):
        if self.nombre == "Gran Conquistador" or self.multiverso == "616" or "El que permanece" in self.descripcion:
            return 3
        elif self.nombre == "Khan que todo lo sabe" or "Carnicero de Dioses" in self.descripcion or self.multiverso == "838":
            return 2
        else:
            return 1

bitacora = []

def agregar_pedido(nombre, multiverso, descripcion):
    nuevo_pedido = Pedido(nombre, multiverso, descripcion)
    prioridad = nuevo_pedido.determinar_prioridad()
    if prioridad == 3:
        bitacora.insert(0, nuevo_pedido)
    elif prioridad == 2:
        bitacora.insert(len(bitacora) // 2, nuevo_pedido)
    else:
        bitacora.append(nuevo_pedido)

def atender_pedido():
    if bitacora:
        pedido = bitacora.pop(0)
        print("Atendiendo pedido de {} del multiverso {}:\n{}".format(pedido.nombre, pedido.multiverso, pedido.descripcion))
    else:
        print("No hay pedidos pendientes en la bitácora.")
