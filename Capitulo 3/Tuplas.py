#las tuplas on listas inmutables, son listas que no se pueden modificar a lo largo del programa

tupla = (1,2,"Hola")
print(tupla)

#si se requiere cambiar de una tupla a una lista
lista = list(tupla)
print(lista)

#en la impresion se puede ver que cambia de parentesis a corchetes

#transformar de lista a tupla
lista = [1,2,3]
tupla = tuple(lista)
print(tupla)

#la tupla consume mucho menor memoria que las listas