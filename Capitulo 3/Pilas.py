#Primero en entrar ultimo en salir, ultimo en entrar primero en salir

pila = [1,2,3]#esto es una lista

#Podemos utilizar la lista como si fuera una pila
print(pila)

#agregando elementos por el final
pila.append(4)
pila.append(5)
print(pila)

#sacando elementos por el final
pila.pop()
print(pila)

#para ver el elmento que estamos sacando
n=pila.pop()
print(f"Sacando el elemento {n}")

print(pila)