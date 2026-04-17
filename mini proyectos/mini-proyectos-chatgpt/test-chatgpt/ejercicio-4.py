vocals = ["a", "A", "e", "E", "i", "I", "o", "O", "u", "U"]
word = input("Ingrese una palabra o cadena de texto: ")
count = 0

for v in word:
    if v in vocals:
        count += 1

print(f"La palabra o cadena de texto: {word}. Tiene {count} vocales")

# este me costo un poco porque no he usado tanto el bucle for pero no me fue el mas complicado
