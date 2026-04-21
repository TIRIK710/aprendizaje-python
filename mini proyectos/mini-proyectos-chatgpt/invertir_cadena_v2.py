"v2: Invertir una cadena utilizando el método reverse() de las listas"

cadena = input("ingrese un texto: ")
cadena2 = []

for letra in cadena:
    cadena2.append(letra)

cadena2.reverse()
print(''.join(cadena2))
