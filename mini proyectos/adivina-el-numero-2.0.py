import random

# usuario elije dificultad
dificultad = str(input("""elige la dificultad:
Facil (F)
Normal (N)
Dificil (D)
""")).lower()

# define la dificultad elejida (numero minimo, numero maximo, intentos disponibles)


def modo_dificultad(elegir):
    if dificultad == "f":
        return 1, 10, 3
    elif dificultad == "n":
        return 1, 50, 7
    elif dificultad == "d":
        return 1, 100, 10
    else:
        exit("ERROR. ingrese una dificultad existente")


# variables
minimo, maximo, max_intentos = modo_dificultad(dificultad)
numero_random = random.randint(minimo, maximo)
contador = 0
# intentos del usuario (dependiendo de la dificultad elejida)
contador_intentos = max_intentos

# bucle_jugable
while contador < max_intentos:  # cuando el numero de iteraciones del bucle sea mayor o igual al numero maximo de intentos el bucle se detendra
    eleccion = int(input(f"""Elige un numero del {minimo} al {maximo}. Numero de intentos: {contador_intentos}
"""))

    if eleccion == numero_random:
        print(
            f"Correcto. El numero era {numero_random}. Intentos sobrantes: {contador_intentos - 1}")
        break  # termina el programa cuando se cumple esta condicion

    contador += 1  # cuenta cada iteracion del bucle
    contador_intentos -= 1  # reduce el numero de intentos que le quedan al usuario

    if eleccion > numero_random:
        print("Muy alto. Intenta otra vez.")

    else:
        print("Muy bajo. Intenta otra vez.")
else:
    print(
        f"Se acabaron los intentos. Perdiste. El número era {numero_random}.")
