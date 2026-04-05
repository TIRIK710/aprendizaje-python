# operadores logicos

# and

edad = 22

print(edad > 18 and edad < 30) # True porque edad es mayor que 18 y menor que 30 

print(edad > 18 and edad > 30) # False porque edad es mayor que 18 pero NO mayor que 30

print(edad < 18 and edad < 30) # False porque edad NO es menor que 18 aunque SI sea menor de 30

print(edad < 18 and edad > 30) # False porque edad NO es menor que 18 ni TAMPOCO es mayor que 30

# El operador lógico and en Python devuelve True solo si 
# ambas expresiones que conecta son verdaderas, y False si 
# al menos una es falsa. Se utiliza para combinar 
# condiciones en estructuras de control (como if o while), 
# evaluando de izquierda a derecha y deteniéndose si 
# encuentra un valor falso. 

# Ejemplo básico
edad = 25
tiene_licencia = True
puede_conducir = (edad >= 18) and tiene_licencia # Resultado: True [11]

# Ejemplo con and de corto circuito (si la primera es falsa, no evalúa la segunda)
x = 0
resultado = (x > 0) and (10 / x > 1) # Resultado: False (no da error de división por cero)

# Características clave del operador and:

    # Conjunción lógica: Requiere que todas las condiciones 
    # sean verdaderas.
    
    # Evaluación perezosa (Short-circuit): Si el primer 
    # operando es falso (False), el operador devuelve ese 
    # primer valor y no evalúa el segundo.
    
    # Valores no booleanos: Si ambos valores son verdaderos 
    # (True), devuelve el último valor evaluado.
    
    # Precedencia: Tiene menor prioridad que los operadores 
    # de comparación (<, >, ==), por lo que se recomienda 
    # usar paréntesis para mayor claridad. 

# or

edad = 22

print(edad > 18 or edad < 30) # True porque edad es mayor que 18 y menor que 30 (ambos son True)

print(edad > 18 or edad > 30) # True porque edad es mayor que 18 aunque NO sea mayor que 30 (uno es True)

print(edad < 18 or edad < 30) # True porque edad NO es menor que 18 pero SI menor de 30 (uno es True)

print(edad < 18 or edad > 30) # False porque edad NO es menor que 18 ni TAMPOCO es mayor que 30 (ninguno es True/ambos son False)

# or en Python evalúa dos expresiones y devuelve True si al
# menos una de ellas es verdadera. Solo devuelve False si
# ambas expresiones son falsas. Es un operador de
# cortocircuito, lo que significa que si la primera
# expresión es verdadera, no evalúa la segunda y devuelve
# True inmediatamente.

# Características clave de or:

    # Sintaxis: expresión1 or expresión2
    # Resultados:
        # True or True -> True
        # True or False -> True
        # False or True -> True
        # False or False -> False
    
    # Comportamiento de cortocircuito: En 42 or [], como 42
    # es verdadero (truthy), devuelve 42 sin evaluar [].

    # Uso: Ideal para estructuras condicionales (if, while)
    # donde se necesita cumplir al menos una de varias
    # condiciones. 

# Ejemplo de código:

edad = 15
tiene_permiso = True

# Se cumple si el usuario es mayor de edad O tiene permiso
if edad >= 18 or tiene_permiso:
    print("Acceso permitido")
else:
    print("Acceso denegado")
# Resultado: Acceso permitido

# not

edad = 22

print(not (edad > 18), not (edad < 30)) # ambos son False porque not cambio el boolean al opuesto. True -> False

print(not (edad > 18), not (edad > 30)) # el primero es False y el segundo es True porque not cambio el boolean al opuesto. True -> False y False -> True

print(not (edad < 18), not (edad < 30)) # el primero es True y el segondo es False porque not cambio el boolean al opuesto. True -> False y False -> True

print(not (edad < 18), not (edad > 30)) # ambos son True porque not cambio el boolean al opuesto. False -> True

# El operador lógico not en Python es una palabra clave unaria que invierte el valor
# de verdad de una expresión booleana: convierte True en False y False en True. Se
# utiliza principalmente para negar condiciones en sentencias if y bucles while,
# comprobando si una condición no se cumple. 

# Características y usos clave:

    # Negación lógica: not True devuelve False, y not False devuelve True.
    
    # Sintaxis: Se coloca antes de la expresión a negar, por ejemplo:
    # if not usuario_activo:.
    
    # Evaluación de falsedad: Funciona con cualquier objeto, devolviendo True si el
    # objeto es intrínsecamente falso (como None, 0, listas vacías [],
    # cadenas vacías "").
    
    # Doble negación: Usar not not revierte el valor al original (ej. not not True
    # es True). 

# Ejemplos de código:

# Ejemplo básico
es_mayor = True
print(not es_mayor)  # Resultado: False

# Uso en sentencias if
lista_vacia = []
if not lista_vacia:
    print("La lista está vacía")  # Se imprimirá esto

# Invertir una comparación
edad = 15
if not edad >= 18:
    print("Es menor de edad")
