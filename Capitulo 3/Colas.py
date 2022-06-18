#el primero en entrar es el primero en salir

cola = ["Maria","Fermin","Alejandro"] #una lista para simular la cola

#agregamos elementos al final de la cola
cola.append("Karla")
cola.append("Flor")

print(cola)

#sacamos elementos por el principio de la cola
n= cola.pop(0)

print(f"Estan atendiendo a {n}")

from collections import deque #esto es para la cola pero es lo mismo que se hace con las listas

