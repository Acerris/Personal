#variables
lista1 =["Fermin","Renold","Ayeleth","Jeisson"]

lista2 =["Jonathan","Renold","Jeisson"]

#Eliminar los elemento repetido
a = set(lista1)
b = set(lista2)

c = list(a | b)

print(f"Lista de elementos que aparecen en las dos listas {c}")

d = list(a - b)
print(f"Los elementos que estan en la lista 1 que no estan en la lista 2 son {d}")


f = list(b - a)
print(f"Los elementos que estan en la lista 2 que no estan en la lista 1 son {f}")

n = list(a & b)
print(f"Los elementos que aparecen en ambas listas son: {n}")