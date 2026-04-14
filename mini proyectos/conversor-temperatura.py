Num1 = float(input("grados a convertir"))

while True:
    
    Num2 = input("unidad a convertir: Celcius-Fahrenheit o Fahrenheit-Celcius").lower()
    
    if num2 == "fahrenheit-celcius":
        Resultado = num1 - 32 / 1.8
        Break
    elif num2 == "celcius-fahrenheit":
        Resultado = num1 * 1.8 + 32
        Break
    else:
        Print("eso no tiene sentido")