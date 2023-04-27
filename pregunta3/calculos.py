from operaciones import *


arbol_suma=Arbol()
arbol_resta=Arbol()
arbol_multiplicacion=Arbol()
arbol_division=Arbol()


a,b,c,d=(10,5,0,"Hola")
arbol_suma.agregar((a))
arbol_suma.agregar((b))
arbol_resta.agregar(str(b))
arbol_resta.agregar(d)
arbol_multiplicacion.agregar(b)
arbol_division.agregar(a)
arbol_division.agregar(c)



print(arbol_suma.sumar())
print(arbol_resta.restar())
print(arbol_multiplicacion.multiplicar_por_si_mismo())
(arbol_division.dividir())