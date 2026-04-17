print("este programa sumara los numeros que ingreses y se detendra cuando escribas el numero 0")
num = int(input("ingrese un numero: "))
suma_num = num

while num != 0:
    print(f"la suma actual es: {suma_num}")
    num = int(input("ingrese otro numero: "))
    suma_num += num
print(
    f"La suma total es: {suma_num}. Y como haz ingresado {num} el programa se ha detenido")

# este no me costo mucho porque ya he usado while varias veces
