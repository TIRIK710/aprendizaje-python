# como yo lo hice

a = 3
b = 4

print(f"3 mayor que 4:", a > b)
print(f"3 menor que 4:", a < b)
print(f"3 mayor o igual a 4:", a >= b)
print(f"3 menor o igual a 4:", a <= b)
print(f"3 igual a 4:", a == b)

# correjido

print(f"{a} mayor que {b}: {a > b}")
print(f"{a} menor que {b}: {a < b}")
print(f"{a} mayor o igual a {b}: {a >= b}")
print(f"{a} menor o igual a {b}: {a <= b}")
print(f"{a} igual a {b}: {a == b}")

# en el primero yo estaba poniendo valores a mano en el
# texto cuando podria haber usado las variables que ya
# tenia aparte de que no usar las variables estaba
# desaprovechando f-string. ahora si cambio los valores 
# de las variables los resultados no seran incoherentes