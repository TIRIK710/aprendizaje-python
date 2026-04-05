resultado = input("Ingresa tu edad: ")
print(type(resultado))
numero = int(resultado)
print(numero + 5)

# int()

# Esta int()función convierte un número o una cadena de caracteres a su equivalente
# entero.
# Ejemplo

# converting a floating-point number to its equivalent integer

result = int(9.9)
print('int(9.9):', result)    # int(9.9): 9

# Sintaxis de int()

# La sintaxis del int()método es:

# int(value, base [optional])

# int() Parámetros

# int()El método toma dos parámetros:

#     valor- cualquier cadena numérica, objeto similar a bytes o un número
#     base [opcional]- el sistema numérico en el que se encuentra actualmente el
#     valor

# int() Valor de retorno

# El int()método devuelve:

#     Parte entera del número: para un único valor de argumento (cualquier número)

#     0 - sin argumentos

#     Representación entera de un número con una base dada (0, 2, 8, 10, 16)

# Ejemplo 1: Python int() con un solo argumento

# int() with an integer value
print("int(123) is:", int(123))

# int() with a floating point value
print("int(123.23) is:", int(123.23))

# int() with a numeric-string value
print("int('123') is:", int("123"))

# Producción

# int(123) es: 123
# int(123.23) es: 123
# int('123') es: 123

# En el ejemplo anterior, hemos devuelto el equivalente entero de un número entero,
# un número decimal y un valor de cadena.

# Ejemplo 2: int() con dos argumentos

# converting a string (that is in binary format) to integer
print("For 0b101, int is:", int("0b101", 2))

# converting a string (that is in octal format) to integer
print("For 0o16, int is:", int("0o16", 8))

# converting a string (that is in hexadecimal format) to integer
print("For 0xA, int is:", int("0xA", 16))

# Producción

# Para 0b101, int es: 5
# Para 0o16, int es: 14
# Para 0xA, int es: 10

# Ejemplo 3: int() para objetos personalizados

# Aunque un objeto no sea un número, podemos convertirlo en un objeto entero.

# Podemos hacerlo fácilmente sobrescribiendo __index__()los __int__()métodos de la
# clase para que devuelvan un número.

# Los dos métodos son idénticos. La versión más reciente de Python utiliza el
# __index__()método.

class Person:
    age = 23

    def __index__(self):
        return self.age

    # def __int__(self):
    #     return self.age

person = Person()


             # int() method with a non integer object person
print("int(person) is:", int(person))
             

# Producción

# int(persona) es: 23

# En el ejemplo anterior, la clase Personno es de tipo entero.

# Pero aún podemos devolver eledadvariable (que es un entero) usando el int()método.

#str()

# La función str() en Python convierte cualquier objeto (números, listas,
# diccionarios) en su representación de cadena de texto (string), facilitando la
# concatenación con otros textos, la impresión en consola o la manipulación de datos
# legibles por humanos. Es esencial para evitar errores al intentar sumar números y
# texto directamente. 

# Características y usos de str():

#    Conversión Básica: Convierte tipos de datos, por ejemplo: str(10) devuelve "10".

#    Concatenación: Permite unir texto con variables numéricas: "Edad: " + str(25).

#    Representación legible: Genera una cadena amigable para el usuario, distinta
#    de repr() que es para depuración.

#    Sintaxis: str(objeto, encoding='utf-8', errors='strict'). 

# Parámetros:

#    objeto (opcional): El valor que se va a convertir. Puede ser cualquier objeto
#    de Python (por ejemplo, int, float, list, dict, bytes).

#    Codificación (opcional): Se utiliza únicamente al convertir desde bytes.
#    El valor predeterminado es 'utf-8'.

#    errores (opcional): especifica cómo manejar los errores de decodificación:

#        'strict': Genera un error (predeterminado).
#        'ignorar': Omite los caracteres no válidos.
#        'reemplazar': Reemplaza los caracteres no válidos con ?.

# Tipo de retorno:

#    Devuelve una representación en cadena del objeto.
#    Devuelve una cadena vacía "" si no se pasa ningún argumento.

# Para más información, puedes consultar la documentación oficial sobre Strings en
# Python. El tipo de dato str y sus operaciones o el tutorial de Strings de Python
# de Google for Developers. 

# Ejemplos:

# Convertir entero a cadena
edad = 30
mensaje = "Tengo " + str(edad) + " años." # "Tengo 30 años."

# Convertir lista a cadena
lista = [1, 2, 3]
cadena_lista = str(lista) # "[1, 2, 3]"

# La función str() es fundamental para la manipulación de texto en Python, como se
# explica en Strings en Python. El tipo de dato str y sus operaciones. Para un
# aprendizaje más profundo, puedes revisar el tutorial de Cadenas de Python

#float()

# En Python, la función float() se utiliza para convertir números o cadenas numéricas
# en números de coma flotante. Un número de coma flotante es simplemente un número
# con un punto decimal (por ejemplo, 3.14, -0.5 o 10.0). Esta función es especialmente
# útil al trabajar con datos introducidos por el usuario o cuando se requieren
# cálculos decimales precisos.

# Ejemplo:

# Input: 10
# Output: 10.0

# Sintaxis

# La función float() en Python tiene la siguiente sintaxis:

#     float(x)

# Parámetro: x (opcional) puede ser un número (entero o decimal), una cadena que
# represente un número, como "10.5" o "inf", "infinito" o "nan".

# Valor de retorno:

#     Devuelve un número de punto flotante correspondiente a x.

#     Si no se pasa ningún argumento, devuelve 0.0.

#     Si una cadena no representa un número válido, se produce un error ValueError.

#     Si un número es demasiado grande, se produce un error de desbordamiento
#     (OverflowError).

# Conversión de enteros a números de coma flotante.

# Se puede convertir fácilmente un número entero en un número de coma flotante envolviéndolo con la función float().

# Ejemplo: En este ejemplo, pasamos un valor de tipo entero a la función float().

number = 90
result = float(number)
print(result)

# Output

# 90.0

# Conversión de cadenas a números de coma flotante.

# Si una cadena contiene valores numéricos, float() puede convertirla en un número
# de punto flotante.

# Ejemplo: Este código convierte cadenas numéricas (tanto de tipo entero como de
# tipo decimal) en números de coma flotante.

string = "90"  # String representing an integer
result1 = float(string)

float_string = "-16.54"  # String representing a float
result2 = float(float_string)

print(result1)
print(result2)

# Output

# 90.0
# -16.54

# Infinito y Nan

# Python permite el uso de números infinitos e indefinidos mediante float().

# Ejemplo: En este ejemplo, pasamos valores infinitos y NaN a la función float() y
# luego imprimimos sus valores float equivalentes.

print(float("inf"))  # Infinity

print(float("infinity"))

print(float("nan"))  # Not-a-Number

print(float("NaN"))


# Output

# inf
# inf
# nan
# nan

# Explicación:

#    "inf" o "infinito": representa el infinito positivo.

#    "-inf": representa el infinito negativo.

#    "nan" (No es un número): representa valores indefinidos, como resultados de
#    operaciones matemáticas no válidas.

#    Estas cadenas no distinguen entre mayúsculas y minúsculas.

# Excepciones y errores

# En ocasiones, la función float() de Python puede no ser compatible con todos los
# tipos de datos. En ese caso, puede generar una excepción o un error.

# 1. ValueError

# La función float() de Python generará un ValueError si el parámetro pasado no es
# un valor numérico.

# Ejemplo: En este ejemplo, pasamos una cadena de letras como parámetro a la función
# float().

number = "geeks"

try:

    print(float(number))

except ValueError as e:

    print(e)

# Output

# could not convert string to float: 'geeks'

# 2. Error de desbordamiento

# La función float() en Python generará un OverflowError si el parámetro pasado es
# demasiado grande.

# Ejemplo: Este código genera un OverflowError porque 10**309 excede el rango de punto
# flotante de Python.



print(float(10**309))

# Output

#     Traceback (most recent call last):
#       File "/home/1eb6a2abffa536ccb1cae660db04a162.py", line 1, in <module>
#         print(float(10**309))
#     OverflowError: int too large to convert to float

#bool()

# La función bool() en Python convierte un valor a booleano (True o False) según su
# "valor de verdad". Retorna False para valores vacíos, 0, None o False; y True
# para cualquier número distinto de cero, cadenas no vacías o estructuras con
# elementos. Es útil para evaluar si una variable tiene contenido. 

# Uso de la función bool():

#    bool(0) = False (el cero es falso)
#    bool(1) = True
#    bool("Hola") = True (cadenas con texto)
#    bool("") = False (cadenas vacías)
#    bool([]) = False (listas vacías)
#    bool([1, 2]) = True (listas con elementos)
#    bool(None) = False 

# Características Clave:

#    Verificación: Como se explica en este artículo de Mimo sobre valores booleanos, 
# la función bool() evalúa si una expresión o variable es verdadera.
#    
#    Valores falsos comunes: El valor 0 (entero o punto flotante), None, listas
# vacías [], diccionarios vacíos {}, tuplas vacías () y cadenas
# vacías "" devuelven False.
#    
#    Subclase de int: En Python, bool es una subclase de int. True equivale a
# 1 y False a 0.
#    
#    Uso común: Se utiliza mucho en la evaluación de expresiones dentro de
# sentencias condicionales if o bucles while