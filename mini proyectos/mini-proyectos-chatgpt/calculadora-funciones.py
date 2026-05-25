# available operations
operaciones = ["+", "-", "x", "/"]

# functions
def sumar(sum1, sum2):
    result = sum1 + sum2
    return result

def restar(res1, res2):
    result = res1 - res2
    return result

def multiplicar(mul1, mul2):
    result = mul1 * mul2
    return result

def dividir(div1, div2):
    if div1 == 0 and div2 != 0:
        result = div1 / div2
        return result
    elif div1 != 0 and div2 == 0:
        return "Indeterminado"
    else:
        result = div1 / div2
        return result

# menu
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

    # close app
    close = input("Desea volver al inicio? Y/N: ").lower()

    if close == "y":
        continue
    elif close == "n":
        print("Cerrando...")
        break
    else:
        print("Accion no reconocida. Intentalo denuevo")