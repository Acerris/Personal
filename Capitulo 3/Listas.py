#Listas
#las listas son como los vectores comienzan desde el indice 0
lista =["Lunes","Martes","Miercoles","Jueves","Viernes",12,True] #puedo colocar cualquier tipo de dato

print(lista)

#agregar un elemento al final de la lista
lista.append(6)

#para agregar un valor en una ubicacion exacta, en la ubicacion 2 agregaremos el valor 3
lista.insert(2,3)

#agrega otra lista al final de la primera lista
lista.extend([6,7,8])

print(lista)

#Imprime lo que se encuentra el indice 0
print(lista[0])
#Imprime del indice 0 hasta el indice 3 + 1
print(lista[0:4])
print(lista[:4])
#Imprime el ultimo indice de la lista
print(lista[-1])
print(lista[-3])
#Imprime desde el indice 2 hasta el final de la lista
print(lista[2:])

#Para calcular cuantos elementos hay en una lista
print(len(lista))

#concatenar listas
lista1 = [1,2,3,4,5]
lista2 = [6,7,8,9,10]
lista3 = lista1 + lista2

print(lista3)

#buscar un valor en la lista
#forma 1
valor = (3 in lista3)
print(valor)
#forma 2
print(3 in lista3)

#esta funcion te dira en indice se encuentra el numero 6
print(lista3.index(6))


#esta funcion count te mostrara la cantidad de veces que se repite el 1 en la lista
lista = [1,1,2,3,4,5,8,9,1]
print(lista.count(1))

#funcion para eliminar el ultimo digito de la lista
lista.pop()

#esta funcion elimina el indice que le indiques
lista.pop(6)
print(lista)

#esta funcion borra el valor que le indiques
lista.remove(5)

#funcion para limpiar la lista o eliminarla completa
print(lista.clear())

#funcion para poner reversa la lista
lista = [1,2,3]
lista.reverse()
print(lista)

#hacer que una lista se duplique
lista = [1,2,3] * 2 
print(lista)

#hacer que se arregle de menor a mayor
lista = [5,9,1,2,4,3]
print(lista)
lista.sort()
print(lista)

#hacer que se arregle de mayor a menor
lista.sort(reverse=True)
print(lista)