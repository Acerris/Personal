#argumentos por valor
#aqui se le pasa una copia no la variable en si
#si se da cuenta aqui no se modifica n, n sigue tenien el mismo valor
"""def doblar_valor(numero):
    numero *= 2
    print(numero)
n = 5
doblar_valor(n)"""

#aqui si se modifica el valor de n
def doblar_valor(numero):
    return numero * 2
n = 5
n = doblar_valor(n)
print(n)

#argumentos por referencia
#en python todas las coleciones se pasan los valores por referencia, osea automatico
def doblar_valores(numeros):
    for i,n in enumerate(numeros):
        numeros[i]*=2

n = [5,10,15,20]

doblar_valores(n)

print(n)

#si requiero pasar una lista por valor y no por referencia hago lo siguiente
def doblar_valores(numeros):
    for i,n in enumerate(numeros):
        numeros[i]*=2

n = [5,10,15,20]

doblar_valores(n[:])#solo cambio esto y automatica le mandare una copia a la funcion

print(n)
