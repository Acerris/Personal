frase = input("Ingrese la frase: ")
frase2 =""
for i in frase:
    if i !=" ":
        frase2 += i#aqui va a concatenarse y se guardara dentro de frase 2 cada elemento 

frase = frase2

n = len(frase)
print(f"La frase es: {frase}")
print(f"la cantidad de letras que no son espacios son: {n}")