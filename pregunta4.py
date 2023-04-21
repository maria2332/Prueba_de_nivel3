import random
import math

def leer_numero(ini, fin, mensaje):
    while True:
        try:
            num = int(input(mensaje))
            if num < ini or num > fin:
                print("Error: el número debe estar entre {} y {}".format(ini, fin))
            else:
                return num
        except ValueError:
            print("Error: debes introducir un número entero")

def generador():
    numeros = leer_numero(1, 20, "¿Cuantos números quieres generar? [1-20]: ")
    modo = leer_numero(1, 3, "¿Cómo quieres redondear los números? [1]Al alza [2]A la baja [3]Normal: ")
    lista_numeros = [random.uniform(0, 100) for _ in range(numeros)]
    if modo == 1:
        lista_redondeada = [math.ceil(num) for num in lista_numeros]
    elif modo == 2:
        lista_redondeada = [math.floor(num) for num in lista_numeros]
    else:
        lista_redondeada = [round(num) for num in lista_numeros]
    for i in range(numeros):
        print("Número original: {}, Número redondeado: {}".format(lista_numeros[i], lista_redondeada[i]))
    return lista_redondeada

if __name__ == "__main__":
    generador()
