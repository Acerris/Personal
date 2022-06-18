#el for se utiliza con colecciones

#El for imprimira por cantidad de elementos

for i in [1,2,3,4,5,"Fermin",True]:
    print(f"elemento: {i}")
#-----------------------------------------------------------------------------------------------------------------------
#otro ejemplo con listas
coleccion = [1,2,3,4,5,"Fermin",True,"Pitti"]

for i in coleccion:
    print(f"listas: {i}")
#-------------------------------------------------------------------------------------------------------------------------
#otro ejemplo con tuplas
coleccion = (1,2,3,4,5,"Fermin",True,"Pitti")

for i in coleccion:
    print(f"tuplas: {i}\n\n")

#--------------------------------------------------------------------------------------------------------------------------
#ejemplo con Diccionarios
Diccionarios= {"Fermin":22,"Maria":23,"Alejandro":22}

for i in Diccionarios:
    print(f"Clave: {i}")#Mostrara solo las claves
    print(f"valor: {Diccionarios[i]}")#Mostrara solo los valores de las claves
    print(f"Clave : {i} ---> valor: {Diccionarios[i]}")#Otra forma de Impresion la cual junta a las dos de arriba
    print(Diccionarios)#Imprimes todo el diccionario

#---------------------------------------------------------------------------------------------------------------------------------
#Diccionarios de una mejor forma
Dic= {"Fermin":22,"Maria":23,"Alejandro":22}

for clave,valor in Dic.items():
    print(f"\n{clave} -> {valor}")

#---------------------------------------------------------------------------------------------------------
#OTRO EJEMPLO

variable = "Fermin"

for i in variable:
  #  print(f"{i}")#imprimira letra por letra con un salto de linea
    print(f"{i}", end= " ")#para que no se haga un salto de linea, se puede colocar un espacio, incluso u punto, lo que quieras