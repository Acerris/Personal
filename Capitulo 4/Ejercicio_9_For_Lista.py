
"""
Forma 1
frase = input("Ingrese la frase: ")
lista = []

for i in frase:
    lista.append(i)

conjunto = set (lista)
lista = list(conjunto)
print(lista)
"""
frase = input("Ingrese la frase: ")
lista = []

for i in frase:
    if i not in lista:
        lista.append(i)
print(lista) #Si lo hago de esta forma si sale ordenado