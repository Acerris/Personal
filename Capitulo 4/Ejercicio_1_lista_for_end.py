#LLenar una lista con los numero del 1 al 50 y luego mostrarlos con un bucle for

lista = []
for i in range(1,51):
    lista.append(i)

for i in lista:
    print(i,end=" - ")


#otra forma mas facil y con menos codigo
lista = list(range(1,51))
for i in lista:
    print(i,end="-")