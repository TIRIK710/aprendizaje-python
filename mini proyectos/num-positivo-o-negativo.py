"""
verifica si un numero es
positivo o negativo
"""


def numero():
    ingreso = input("ingrese el numero que desea comprobar: ")
    return ingreso


while True:
    num = numero()
    if num == "0":
        print(num, "es neutro.")
    elif num == "-0":
        print(num, "no exciste")

    try:
        conv = float(num)
    except ValueError as e:
        print(f"Error: {e}")
        continue
    else:
        if conv > 0:
            print(conv, "es positivo.")
        elif conv < 0:
            print(conv, "es negativo.")
    break
