#conjuntos
#si no se coloca el set no es un conjunto
conjunto = set()

#conjuntos vacios\ si no le colocamos el {} seria un diccionario
conjunto = {1,2,3}#no puede haber otro tipo de coleccion dentro del conjunto (coleccion me refiero a tuplas o lista)

print(conjunto)

#en el conjunto no se guardan valores duplicados
prueba = set()
prueba = {1,2,3,1}
print(prueba)

#para aniadir un valor al conjunto utilizamos la funcion add(), el no lo colocaral final, el colocara el dato donde el quiera
prueba.add(5)
print(prueba)

#para eliminar un valor del conjunto
prueba.discard(1)
print(prueba)

#para saber si el 3 no esta en el conjunto
print(3 not in prueba)

#Prueba 1
if len(prueba) == len(conjunto):
    print("True")
else:
    print(False)

#para eliminar el conjunto o limpiarlo
conjunto.clear

#conjuntos Parte 2
#la funcion set() solo funciona en caso de que se cree un conjunto vacio y quisieras agregar elementos
# si ya le pones los elementos desde el inicio python ya sabe que es un conjunto
 
#esto sirve para comparar dos conjuntos
a = {1,2,3}
b = {4,5,6}
print(a==b)
# no podemos utilzar c = a + b para cocatenar los conjuntos ya que esto solo funciona en las listas
 
#La union
conjuntoa = {1,2,3}
conjuntob = {3,4,5}
c = conjuntoa | conjuntob  #aqui va a concatenar los datos pero los duplicados solo los pondra una vez
print(c)
 
#la interseccion
conjuntoa = {1,2,3}
conjuntob = {3,4,5}
c = conjuntoa & conjuntob
print(c)
 
#la diferencia
conjuntoa = {1,2,3}
conjuntob = {3,4,5}
c = conjuntoa - conjuntob #imprimira los conjuntos en a que no estan en b
print(c)
 
#diferencia simetrica
conjuntoa = {1,2,3}
conjuntob = {3,4,5}
c = conjuntob ^ conjuntoa #imprimira los conjuntos en a y en b que no estan en la interseccion
print(c)
 
#subconjunto
a = {1,2,3}
b = {3,4,5}
c = {1,2,3,4,5}
print(a.issubset(c)) #Aqui indicamos si el conjunto a es un subconjunto de C el cual es verdadero

#superconjunto
a = {1,2,3}
b = {3,4,5}
c = {1,2,3,4,5}
print(c.issuperset(a)) #Aqui indicamos si c es un superconjunto de a ya que en c estan todos los elementos de a

#disconexos
print(a.isdisjoint(b))#aqui indica si son disconectos, ose disconexos es si no comparten un valor en comun


#conjuntos inmutables = no podemos modificar el conjunto
a = frozenset({1,2,3}) #los conjuntos inmutables son como las tuplas
b = {3,4,5}
c = {1,2,3,4,5}
print(c.issuperset(a))