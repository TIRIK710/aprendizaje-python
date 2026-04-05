# Ejercicio 1: La función "Eco" (Sin return)

# Crea una función llamada repetir_mensaje que reciba un parámetro (un texto) y lo
# imprima 3 veces seguidas.

   # Objetivo: Practicar cómo el parámetro viaja desde afuera hacia adentro de la
   # función.

   # Pista: Puedes usar un bucle for o simplemente tres print().

#definimos
def repetir_texto(mensaje):
#   proceso
    print(mensaje)
    print(mensaje)
    print(mensaje)

#llamamos a la funcion
repetir_texto("hola mundo")

# segundo ejemplo

#definir
def repetir_mensaje(texto):
    #proceso
    for i in range(3):
        #proceso2
        print(texto)
#llamada
repetir_mensaje("este es un bucle")

# Ejercicio 2: El Conversor de Edad (Uso de int y return)

# Crea una función llamada calcular_nacimiento que reciba un parámetro llamado edad.
# La función debe devolver (return) el año en que nació la persona (asumiendo que 
# estamos en 2026).

   # Objetivo: Practicar operaciones matemáticas dentro de una función y devolver un
   # resultado.

   # Pista: 2026 - edad. Recuerda que si usas input() para obtener la edad, debes
   # convertirla a int().

# 1. definicion (la maquina)
def calcular_edad(edad):
    # que va a hacer
    resultado = 2026 - edad
    return resultado

# 2. uso de la funcion
# recibe la edad del usuario
mi_edad = int(input("cuantos años tienes? "))

# luego se lo pasa a la funcion
año_nacimiento = calcular_edad(mi_edad)

# ahora muestra el s=resultado
print("naciste en el año:", año_nacimiento)

# Ejercicio 3: El Validador de Acceso (Lógica y Booleanos)

# Crea una función llamada es_mayor_de_edad que reciba un número.

   # Si el número es 18 o más, debe devolver True.

   # Si es menor, debe devolver False.

   # Objetivo: Aprender a usar if / else dentro de una función.

# definimos la funcion
def es_mayor_de_edad(mayor):
# procesamos lo que hara la funcion cuando sea llamada
    if mayor >= 18:
        return True # la funcion devolvera un "si" (verdadero)
    else:
        return False # la funcion devolvera un "no" (falso)

# 1. pedimos el dato y lo convertimos de str a int
mi_edad = int(input("que edad tienes? "))

# 2. llamamos a la funcion y guardamos el boolean (True/False)
resultado = es_mayor_de_edad(mi_edad)

# 3. ahora con el resultado decidiremos que imprimir
if resultado: # esto significa "si el resultado es True"
    print("¡Acceso concedido! Eres mayor de edad.")
else:
    print("Acceso denegado. Eres menor de edad.")

# Ejercicio 4: Mini Calculadora (Múltiples Parámetros)

# Crea una función llamada operacion que reciba tres parámetros: num1, num2 y tipo.

   # Si tipo es "suma", devuelve la suma.

   # Si tipo es "multiplicacion", devuelve el producto.

   # Objetivo: Manejar varios datos a la vez.

def operacion(num1, num2, tipo):
    if tipo == "suma":
        return num1 + num2
    elif tipo == "multiplicacion":
        return num1 * num2
    else:
        return "operacon no valida"

dato1 = int(input("ingrese el primer dato "))
dato2 = int(input("ingrese el segundo numero "))

tipo_usuario = input("quieres suma o multiplicacion? ")

resultado1 = operacion(dato1, dato2, tipo_usuario)

print(f"el resultado de la {tipo_usuario} es: {resultado1}")