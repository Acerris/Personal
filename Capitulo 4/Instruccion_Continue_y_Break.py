
#Aqui cuando la condicion vea que el iterador i es igual a 5 simplemente le dira continua imprimiendo y en la impresion no se vera el numero 5
for i in range(10):
    if i == 5:
        continue
    print(i, end=".")

for i in range(10):
    if i == 5:
        break # esto solo revienta el for y automaticamente sale 
    print(i)
print("Termino")