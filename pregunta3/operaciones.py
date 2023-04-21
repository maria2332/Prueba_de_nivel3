def suma(num1, num2):
    try:
        resultado = float(num1) + float(num2)
    except TypeError:
        print("Error: Tipo de dato no válido.")
        resultado = None
    return resultado

def resta(num1, num2):
    try:
        resultado = float(num1) - float(num2)
    except TypeError:
        print("Error: Tipo de dato no válido.")
        resultado = None
    return resultado

def producto(num1, num2):
    try:
        resultado = float(num1) * float(num2)
    except TypeError:
        print("Error: Tipo de dato no válido.")
        resultado = None
    return resultado

def division(num1, num2):
    try:
        resultado = float(num1) / float(num2)
        if num2 == 0:
            raise ZeroDivisionError
    except TypeError:
        print("Error: Tipo de dato no válido.")
        resultado = None
    except ZeroDivisionError:
        print("Error: No es posible dividir entre cero.")
        resultado = None
    return resultado
