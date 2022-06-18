print("Hola Mundo")

numero = 10
numero1 = 10

print((numero + numero1)*10)
print(type(numero))
print("------------------------------------------------------------------------------------")
"""Tipdado dinamico """

valor = 10
print(valor)

valor = True
print(valor)

valor = "hola"
print(valor)
print("------------------------------------------------------------------------------------")
#la misma variable puede cambiar de tipo o valor sin problemas


#operadores relacionales
print("Operadores Relacionales")
a = 10
b = 20
c = 30

resultado = a + b == c

print(resultado)
print("------------------------------------------------------------------------------------")
#operadores logicos
print("Operadores Logicos")
a = 10
b = 15
c = 20

resultado = ((a<b) and (b<c))
#><
print(resultado)

print("-----------------------------------------------------------------------------------------------")
#salidas
print("Salidas")
nombre = "Fermin"
edad = 22

#Formas de impresion

#Forma 1
print("hola",nombre,"tienes",edad,"anios")

#Forma 2
print("Hola {} tienes {} anios".format(nombre,edad))

#Forma 3 - Nueva forma 3.6 en adelante - la f al principio del comando es para decirle a python que es la nueva forma de impresion
print(f"Hola {nombre} tienes {edad} anios")

print("---------------------------------------------------------------------------------------------------------------")
#Entrada de datos
print("Entrada de datos")
#Entrada de datos tipo cadena - el Input guarda datos tipo cadena
nombre = input("Digite su nombre: ")
print(f"Hola {nombre}")

#Entrada de datos tipo entero con el float seria lo mismo
nombre = int(input("Digite un numero: ")) #aqui digitas un str pero se convierte en int
print(f"Hola {nombre}")


#Funciones integradas
print("Funciones integradas")
#str para convertir un int o float a str
n= str(10)
print(n)

#para converitr a un binario
n= bin(10)
print(n)

#para converitr a un hexadecimal
n= hex(10)
print(n)

#como convertir un binario a entero
#lleva el binario,la base
n= int("0b1010",2)
print(n)

#mostrar el valor absoluto d un numero
n= abs(10)
print(n)

#forma de redondear un numero
n= round(5.6)
print(n)

#Len funcion que cuenta las cantidades de letra de una palabra
n= len("Fermin")
print(n)

print("--------------------------------------------------------------------------------------------")

#Condicionales
print("Condicionales")
numero = int(input("Coloque el numero: "))

if numero > 0:
    print("El numero es positivo")
elif numero==0:
    print("El numero ingresado es cero")
else:
    print("El numero es negativo")