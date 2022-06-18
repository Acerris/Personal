

lista = []

salir = False

while not salir:
    numeros = int( input("Ingrese el numero: "))
    if (numeros == 0):
        #break o podemos colocar salir = true para que se vuelva false y salga del while
        salir=True
    else:
        lista.append(numeros)

lista.sort()
print(lista)
    