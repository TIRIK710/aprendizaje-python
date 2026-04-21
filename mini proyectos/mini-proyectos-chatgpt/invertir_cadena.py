"v1"

cadena = list(input("ingrese un texto: "))

cadena2 = []

for letra in cadena:
    cadena2.insert(0, letra)

print(''.join(cadena2))
