import random

# usuario elije dificultad
DIFICULTAD = str(input("""elige la dificultad:
Facil (F)
Normal (N)
Dificil (D)
""")).lower()

# define la dificultad elejida (numero minimo, numero maximo, intentos disponibles)


def modo_dificultad(dificultad_elegida):
    """Devuelve el rango y los intentos según la dificultad seleccionada."""
    if dificultad_elegida == "f":
        return 1, 10, 3
    elif dificultad_elegida == "n":
        return 1, 50, 7
    elif dificultad_elegida == "d":
        return 1, 100, 10
    else:
        exit("ERROR. ingrese una dificultad existente")


# variables
minimo, maximo, max_intentos = modo_dificultad(DIFICULTAD)
numero_random = random.randint(minimo, maximo)
CONTADOR = 0
# intentos del usuario (dependiendo de la dificultad elejida)
CONTADOR_INTENTOS = max_intentos

# bucle_jugable
while CONTADOR < max_intentos:  # cuando el numero de iteraciones del bucle sea mayor o igual al numero maximo de intentos el bucle se detendra
    eleccion = int(input(f"""Elige un numero del {minimo} al {maximo}. Numero de intentos: {CONTADOR_INTENTOS}
"""))

    if eleccion == numero_random:
        print(
            f"Correcto. El numero era {numero_random}. Intentos sobrantes: {CONTADOR_INTENTOS - 1}")
        break  # termina el programa cuando se cumple esta condicion

    CONTADOR += 1  # cuenta cada iteracion del bucle
    CONTADOR_INTENTOS -= 1  # reduce el numero de intentos que le quedan al usuario

    if eleccion > numero_random:
        print("Muy alto. Intenta otra vez.")

    else:
        print("Muy bajo. Intenta otra vez.")
else:
    print(
        f"Se acabaron los intentos. Perdiste. El número era {numero_random}.")
