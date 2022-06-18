#los diccionarios tienes dos valores por posicion
#los diccionarios no son ordenados, puede agregar listas, valores, tuplas incluso otros diccionarios
#tiene la forma de clave : valor
disccionario = {}# esto es un diccionario vacio es diferente a conjunto ya que conjunto lleva set()

disccionario1 = {"blue":"azul","red":"rojo","Green":"verde"}

print(disccionario1)#Impresion de todo el diccionario

print(disccionario1["red"])#Impresion especifica

disccionario1["yellow"] = "Amarillo" #Agregar un valor al diccionario

print(disccionario1)

del(disccionario1["Green"])#eliminar un valor del diccionario

print(disccionario1)

#Prueba 2
#       esta parte es un diccionario                 esta parte es una lista
Dic = {"Fermin":{"Edad":22,"Estado Civil":"Soltero"},"Jose":[21,"Casado"],10:"Messi",True:"Verdadero"}
print(Dic["Fermin"])

print(Dic.get("Fermin","No existe en el diccionario"))#Imprimira el valor de la clave Fermin y en caso tal de que no exista retornara el mensaje no existe
print(Dic.get(11,"No existe esta clave")) #Ejemplo , como no existe el 11 retornara el mensaje de no existe

print(10 in Dic)#esto es para indicar si el numero 10 se encuentra dentro del diccionario Dic, mandara mensaje de true o false

print(Dic.keys())#es para imprimir las claves del diccionario
print(Dic.values())#es para imprimir los valores de las claves

print(Dic.items())#lo organiza como si fueran tuplas 
