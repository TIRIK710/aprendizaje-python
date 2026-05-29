# available operations
operaciones = ("+", "-", "*", "/")

# functions
def sumar(a, b):
    return a + b


def restar(a, b):
    return a - b

def multiplicar(a, b):
    return a * b
    

def dividir(a, b):
    if b == 0:
        return "Indeterminado"
    return a / b

def menu():
    while True:
        
        print("Bienvenido a la app Calculadora")

        try:
            num1 = float(input("ingrese el primer numero: "))
        except ValueError:
            print("Caracter invalido")
            continue
        
        operacion = input(f"Ingrese la operacion que desea realizar: {", ".join(operaciones)}: ")
        if operacion not in operaciones:
            print("la operacion ingresada no es valida")
            continue
        
        try:
            num2 = float(input("ingrese el segundo numero: "))
        except ValueError:
            print("Caracter invalido")
            continue
        
        if operacion == "+":
            print(f"el resultado es: {sumar(num1, num2)}")
        elif operacion == "-":
            print(f"el resultado es: {restar(num1, num2)}")
        elif operacion == "*":
            print(f"el resultado es: {multiplicar(num1, num2)}")
        elif operacion == "/":
            print(f"el resultado es: {dividir(num1, num2)}")
        break

menu()

# close app
while True:
    close = input("Desea volver al inicio? Y/N: ").lower()

    if close == "y":
        menu()
    elif close == "n":
        print("Cerrando...")
        break
    else:
        print("Accion no reconocida. Intentalo denuevo")
        continue