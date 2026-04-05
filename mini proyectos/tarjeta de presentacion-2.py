def preguntar(pregunta):
    return input(pregunta + " ")

nombre = preguntar("como te llamas?")

edad = int(preguntar("que edad tienes?"))

presentacion = f"""hola, me llamo {nombre}
tengo {edad} años"""

if edad <= 0:
    print("eso no tiene sentido")
else:
    print(presentacion)