######################################################################################################

"""primer intento"""

# num1 = float(input("grados a convertir: "))

# while True:

#   num2 = input("unidad a convertir: Celcius-Fahrenheit(C) o Fahrenheit-Celcius(F): ").lower()

#  if num2 == "fahrenheit" or num2 == "f":
#     resultado = num1 - 32 / 1.8
#    print(f"{num1} grados fahrenheit equivalen a {resultado:.2f} grados celcius")
#   break
# elif num2 == "celcius" or num2 == "c":
#   resultado = num1 * 1.8 + 32
#  print(f"{num1} grados celcius equivalen a {resultado:.2f} grados fahrenheit")
# break
# else:
#    print("eso no tiene sentido")

#####################################################################################################

# mejora No. 1

lista_unidades = ["celcius", "fahrenheit", "kelvin"]


def unit():
    eleccion_usuario = input("que unidad deseas convertir?: ")
    return eleccion_usuario


while True:
    unidad = unit()

    if unidad not in lista_unidades:
        print("unidad no permitida")
    else:
        break

grados = float(input(f"ingrese los grados {unidad} que desea convertir: "))

if unidad == "kelvin":
    resultado1 = grados - 273.15
    resultado2 = 1.8 * (grados - 273.15) + 32
    print(f"""
    celcius: {resultado1}
    fahrenheit: {resultado2}""")

elif unidad == "fahrenheit":
    resultado1 = (grados - 32) / 1.8
    resultado2 = (grados - 32) / 1.8 + 273.15
    print(f"""
    celcius: {resultado1}
    kelvin: {resultado2}""")

else:
    resultado1 = grados * 1.8 + 32
    resultado2 = grados + 273.15
    print(f"""
    fahrenheit: {resultado1}
    kelvin: {resultado2}""")
