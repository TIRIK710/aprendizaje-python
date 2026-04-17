num1 = int(input("ingrese un numero: "))
num2 = int(input("ingrese otro numero: "))
num3 = int(input("ingrese un ultimo numero: "))

if num1 > num2 and num1 > num3:
    print(f"El numero mayor es {num1}")
elif num2 > num1 and num2 > num3:
    print(f"El numero mayor es {num2}")
else:
    print(f"El numero mayor es {num3}")

# este pense que sabria hacerlo con una lista pero no tengo tan dominado el tema de conjuntos. pero cuando pense en hacerlo con 3 variables no me costo mucho
