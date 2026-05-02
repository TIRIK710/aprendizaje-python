# V1
#saldo = float(input("cuanto es el saldo de tu cuenta?: "))

#while True:
#    propina = float(input("cuanto porcentaje de propina quieres pagar?: "))

#    if propina < 0:
#        print("no le vas a quitar la plata al mesero, mmgvo")
#    else:
#        break

#total = saldo + (saldo *propina / 100)
#print(f"el total a pagar es de: {total}")

####################################################################################

# V2
saldo = float(input("cuanto es el saldo de tu cuenta?: "))
propina = float(input("cuanto porcentaje de propina quieres pagar?: "))

def calcular_propina(saldo, propina):
    total = saldo + (saldo * propina / 100)
    return total

if propina < 0:
    print("no le vas a quitar la plata al mesero, mmgvo")

total_a_pagar = calcular_propina(saldo, propina)
print(f"el total a pagar es de: {total_a_pagar}")