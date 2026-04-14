num1 = float(input("grados a convertir"))

while True:
    
    num2 = input("unidad a convertir: Celcius-Fahrenheit o Fahrenheit-Celcius").lower()
    
    if num2 == "fahrenheit-celcius":
        resultado = num1 - 32 / 1.8
        break
    elif num2 == "celcius-fahrenheit":
        resultado = num1 * 1.8 + 32
        break
    else:
        print("eso no tiene sentido")