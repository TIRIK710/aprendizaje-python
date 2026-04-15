try:
    num = int(input("ingrese un numero: "))
except ValueError:
    print("Error. El numero no debe inclir decimales ni ser ningun otro caracter")
else:
    resultado = num % 2
    if resultado == 1:
        print(f"{num} es impar")
    else:
        print(f"{num} es par")