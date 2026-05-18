print("Bienvenido a la app Calculadora")

num1 = float(input("ingrese el primer numero"))

operacion = input("Ingrese la operacion que desea realizar: (+) (-) (x) (/)")

num2 = float(input("ingrese el segundo numero"))

# functions
def sumar():
    result = num1 + num2
    return result

def restar():
    result = num1 - num2
    return result

def multiplicar():
    result = num1 * num2
    return result

def dividir():
    result = num1 / num2
    return result

