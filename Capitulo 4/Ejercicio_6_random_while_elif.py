#Juego para adivinar numero
import random

numrandom= random.randint(0,100)
n = 0

salir = False
while not salir:
    numero = int(input("Ingrese el numero por adivinar: "))
    if numero == numrandom:
        n+=1
        print(f"Has ganado el numero aleatorio era {numrandom} y el que colocastes fue {numero}")
        print(f"La cantidad de veces que intento fueron {n}")
        salir = True

    elif numero > numrandom:
        n+=1
        print("El numero es mayor")
       
    elif numero < numrandom:
        n+=1
        print("El numero es menor")
    
