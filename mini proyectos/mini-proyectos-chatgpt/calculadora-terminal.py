"""
1. nos pida un primer numero
2. nos pida un segundo numero
3. nos pida una operacion (+ - * /)
"""

lista_operation = ["+", "-", "*", "/"]

num1 = float(input("ingrese el primer numero: "))
num2 = float(input("ingrese el segundo numero: "))
operation = input(f"ingresa una operacion {' '.join(lista_operation)}: ")

while operation not in lista_operation:
    operation = input("ingresa una operacion (+ - * /): ")

try:
    print(eval(f"{num1} {operation} {num2}"))
except ZeroDivisionError:
    print("no se puede dividir por")