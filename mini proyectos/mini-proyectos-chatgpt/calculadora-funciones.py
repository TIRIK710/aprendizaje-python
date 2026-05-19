# available operations
operaciones = ["+", "-", "x", "/"]

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
    if num1 == 0 or num2 == 0:
        return "indeterminado"
    else:
        result = num1 / num2
        return result

# menu
while True:
    
    print("Bienvenido a la app Calculadora")

    num1 = float(input("ingrese el primer numero: "))
    
    operacion = input(f"""Ingrese la operacion que desea realizar: {operaciones}: """)
    if operacion not in operaciones:
        print("la operacion ingresada no es valida")
        continue

    num2 = float(input("ingrese el segundo numero: "))

      
    if operacion == "+":
        print(f"el resultado es: {sumar()}")
    elif operacion == "-":
        print(f"el resultado es: {restar()}")
    elif operacion == "*":
        print(f"el resultado es: {multiplicar()}")
    elif operacion == "/":
        print(f"el resultado es: {dividir()}")
    break