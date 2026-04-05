lenguajes = ["Python", "Ruby", "PHP", "Javascript", "Java"] # lista
print("1.", lenguajes)

lenguajes.insert(3, "Go") # insertar "Go" como 4to elemento de la lista 
print("2.", lenguajes)

lenguajes.insert(0, "C") # insert "C" como 1er elemento de la lista
print("3.", lenguajes)

lenguajes.remove("Ruby") # remover elemento "Ruby" de la lista
print("4.", lenguajes)

print("5.", "PHP" in lenguajes) # buscar si el elemento "PHP" esta en la lista
                                # (True = esta en la lista, False = no esta en la lista)

print("7.", len(lenguajes)) # ver cuantos elementos hay en la lista (6 en este caso)

print("6.", lenguajes.clear()) # vaciar la lista