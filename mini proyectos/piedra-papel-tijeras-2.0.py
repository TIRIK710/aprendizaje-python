import random


def jugar():
    """Simula una ronda del juego de piedra, papel o tijeras."""
    reglas = {  # key gana a value
        "piedra": "tijeras",
        "tijeras": "papel",
        "papel": "piedra"
    }

    while True:
        usuario = input("Elije: piedra, papel o tijeras: ").lower()
        if usuario not in reglas:
            print("Opcion no valida.")
            continue
        else:
            break

    # toma solo las keys del diccionario: reglas{} y luego las convierte en una lista[] y luego elige un elemento al azar de dicha lista
    computadora = random.choice(list(reglas.keys()))
    print(f"Computadora eligio: {computadora}")

    if usuario == computadora:  # si el usuario y la computadora eligieron lo mismo es empate
        print("Empate!")
    # si el value de la key que eligio el usuario es igual a la key que eligio, la computadora gana el usuario
    elif reglas[usuario] == computadora:
        print("Ganaste!")
        return 1
    else:  # si lo que la computadora eligio no es igual a lo que el usuario eligio ni tampoco al value de la key que el usuario eligio, el usuario pierde
        print("Perdiste!")
        return 2


def rondas():
    lista_rondas = ["1", "3", "5", "7"]
    """Solicita al usuario que elija el número de rondas a jugar (1, 3 o 5)."""
    while True:
        elejir = input(f"Cuantas rondas quieres jugar?: {', '.join(lista_rondas)}")
        if elejir not in lista_rondas:
            print("Intenta otra vez")
            continue
        else:
            return int(elejir)


def incrementar(puntaje_usuario, puntaje_computadora, ronda):
    """Incrementa el puntaje del ganador de la ronda."""
    if ronda == 1:
        puntaje_usuario += 1
    elif ronda == 2:
        puntaje_computadora += 1
    return puntaje_usuario, puntaje_computadora


print("""Este juego se llama: Piedra, Papel o Tijeras. Las reglas son las siguientes:
Piedra le gana a Tijeras
Tijeras le gana a Papel
Papel le gana a Piedra
Puedes jugar 1 ronda, 3 rondas o 5 rondas contra la computadora.
El que tenga mas puntos al final gana.
""")

PUNTAJE_USUARIO = 0
PUNTAJE_COMPUTADORA = 0
contador = rondas()

for i in range(contador):
    RONDA = jugar()
    PUNTAJE_USUARIO, PUNTAJE_COMPUTADORA = incrementar(
        PUNTAJE_USUARIO, PUNTAJE_COMPUTADORA, RONDA)

print(f"""nuestros puntos fueron:
computadora: {PUNTAJE_COMPUTADORA}
tu: {PUNTAJE_USUARIO}
""")

if PUNTAJE_USUARIO > PUNTAJE_COMPUTADORA:
    print("eso significa que ganaste")
elif PUNTAJE_USUARIO == PUNTAJE_COMPUTADORA:
    print("eso significa que empatamos")
else:
    print("eso significa que perdiste")

print("presiona cualquier tecla para salir...")
