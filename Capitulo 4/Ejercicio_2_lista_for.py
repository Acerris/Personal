
lista = list(range(1,11))

valor = int(input("Ingrese el numero: "))
lista2 = []

print(f"Lista original {lista}")

for i in lista:
     lista2= i * valor
     print("\n",lista2,end=" ")

#otra forma es:
indice = 0
for i in lista:
    lista[indice] *= valor
    indice += 1
print("\n\n",lista)

#Forma mas facil sin crear indice ni irlo subiendo de valor +1, es lo mismo que arriba, si se requiere usar un indice se usa junto a la funcion enumerate
for indice,i in enumerate(lista):
    lista[indice] *= valor
print(lista)