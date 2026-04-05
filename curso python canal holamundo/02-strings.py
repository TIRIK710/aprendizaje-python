texto = "Hello World"
#        0123456789...   los string cuentan con un indice
#                        basado en 0. de forma que en este caso
#                        al usar la funcion find va a decir que 
#                        la "W" esta en la posicion 6

print(texto) # sin funcion = texto tal cual esta escrito

print(texto.upper()) # funcion upper = todo el texto en mayusculas

print(texto.lower()) # funcion lower = todo el texto en minusculas

print(texto.find("W"))   # funcion find = dice la posicion mas cercana a 0 del caracter indicado, es decir, devuelve el indice
print(texto.find("Hell")) # con cadenas de texto indica la posicion donde esta cadena empieza
                         # TANTO EL CARACTER COMO LA CADENA DE TEXTO TIENEN QUE ESCRIBIRSE CORRECTAMENTE, SINO NO FINCIONA

nuevoTexto = texto.replace("ld", "bro")    # funcion replace = reemplaza los caracteres indicados de la variable string por otros indicados en la funcion
                                           # no cambia la variable
print(texto, nuevoTexto)

print("World" in texto) # in es un operador de pertenencia utilizado para verificar si un valor
                        # o elemento existe dentro de una secuencia (como cadenas, listas o tuplas)
                        # o una colección (diccionarios o conjuntos). Devuelve True si encuentra el valor
                        # y False si no, siendo fundamental en estructuras condicionales y ciclos
                        # a diferencia de find, no devuelve su posicion sino solo si lo encontro o no

# Las funciones en Python son
# bloques de código reutilizables y organizados que realizan una tarea específica, permitiendo estructurar programas de forma eficiente. Se definen usando la palabra clave def, seguidas por el nombre de la función, paréntesis () y dos puntos :, mejorando la legibilidad y evitando la repetición de código. 
# Este video explica cómo definir y utilizar funciones en Python:
# Miniatura de un video relacionado

# Conceptos Clave de Funciones en Python:

#    Definición (def): Se crea la función con un nombre y parámetros opcionales, por ejemplo: def mi_funcion(parametro):.
#    Llamada: Se ejecutan usando su nombre seguido de paréntesis, como mi_funcion().
#    Parámetros y Argumentos: Son las entradas de datos que la función puede recibir para operar.
#    Retorno (return): Especifica el valor que la función devuelve tras ejecutarse. Si no se usa, la función devuelve None por defecto.
#    Funciones Built-in: Python incluye funciones integradas listas para usar, como print(), len(), o sum(). 

# Ejemplo Básico:
# python

# Definición de la función
def saludar(Whatever):
    return f"Hola, {Whatever}!"

# Llamada a la función
mensaje = saludar("Mundo")
print(mensaje) # Salida: Hola, Mundo!

# Ventajas:

#     Reutilización: Escribes el código una vez y lo usas múltiples veces.
#     Organización: Divide programas complejos en partes más pequeñas y manejables.
#     Mantenibilidad: Facilita la depuración y actualización del código. 