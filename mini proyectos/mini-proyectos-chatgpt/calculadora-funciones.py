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

    num1 = float(input("ingrese el primer numero: "))
    
    operacion = input(f"""Ingrese la operacion que desea realizar: {operaciones}: """)
    if operacion not in operaciones:
        print("la operacion ingresada no es valida")
        continue

    num2 = float(input("ingrese el segundo numero: "))

      
    if operacion == "+":
        print(f"el resultado es: {sumar(num1, num2)}")
    elif operacion == "-":
        print(f"el resultado es: {restar(num1, num2)}")
    elif operacion == "*":
        print(f"el resultado es: {multiplicar(num1, num2)}")
    elif operacion == "/":
        print(f"el resultado es: {dividir(num1, num2)}")
    break

    