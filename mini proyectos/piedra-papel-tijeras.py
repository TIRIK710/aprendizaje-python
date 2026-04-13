import random

"piedra" > "tijeras"
"tijeras" > "papel"




contador = 0
intentos = 3

while contador < intentos:

    if contador == 0:
        eleccion = input("piedra, papel o tijeras? ").lower()
    else:
        eleccion = input("Elije otra vez: piedra, papel o tijeras? ").lower()
    oponente = random.choice(["piedra", "papel", "tijeras"])
    
    contador += 1
    
    if eleccion == "papel" and oponente == "piedra":
        print(f"yo eleji {oponente}, y como tu elejiste {eleccion} eso significa que tu ganaste")

    elif eleccion > oponente:
        print(f"yo eleji {oponente}, y como tu elejiste {eleccion} eso significa que tu ganaste")

    elif eleccion == oponente:
        print(f"yo eleji {oponente}, y como tu elejiste {eleccion} eso significa que empatamos")

    else:
        print(f"yo eleji {oponente}, y como tu elejiste {eleccion} eso significa que tu perdiste")
