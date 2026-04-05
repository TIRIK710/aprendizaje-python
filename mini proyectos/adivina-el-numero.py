import random

numero_random = random.randint(1,10)
elec = int(input("elige un numero del 1 al 10: "))

while elec != numero_random:
    elec = int(input("intenta otra vez: "))    

print(f"correcto. el numero era {numero_random}")