temp = float(input("Ingrese una temperatura a convertir: "))
scale = input("Es Fahrenheit(F) o Celcius(C)?: ").lower()

if scale == "f":
    celcius = (temp - 32) * 5/9
    print(celcius)
elif scale == "c":
    fahrenheit = temp * 1.8 + 32
    print(fahrenheit)
else:
    print("escala incorrecta")