num1 = float(input("grados a convertir"))

while True:
    
    num2 = input("unidad a convertir: Celcius-Fahrenheit o Fahrenheit-Celcius").lower()
    
    if num2 == "fahrenheit":
        resultado = num1 - 32 / 1.8
        print(f"{num1} grados celcius equivalen a {resultado} grados fahrenheit")
        break
    elif num2 == "celcius":
        resultado = num1 * 1.8 + 32
        print(f"{num1} grados fahrenheit equivalen a {resultado} grados celcius")
        break
    else:
        print("eso no tiene sentido")