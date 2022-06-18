#Ejercicio 1 -  eliminar valores duplicados de una lista

lista = [1,1,2,3,"Alejandro",4,4,5,9,9,9,9]

conjunto = set (lista)#se convierte a un conjunto y elimina los duplicados
lista = list(conjunto)#se convierte a lista nuevamente

print(lista)

#forma simplificada 
lista = [1,1,2,3,4,4,5,9,9,9,9,6,7,7,7,7,7,7,7,7,7,8,10]
lista = list(set(lista))
lista.sort(reverse=True)#lo coloque solo para que se organizara de mayor a menor
print(lista)

