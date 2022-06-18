#funciones sin retorno de valor

#Crear funcion
#def significa  funcion, luego el nombre que llevara la funcion , y luego vienen los (el cual llevara parametros)
def  saludar():
    #Cuerpo de la funcion
    print("Hola mundo")
saludar()#LLamado de la funcion


#Funcion con parametros
def nombre(nombre):
    print(f"Hola {nombre}")

nombre("Fermin")
nombre("Carlos")

#funcion tabla de multiplicar
numero = int(input("Ingrese el numero que desea multiplicar: "))
def tabla_de_multiplicar(num):
    for i in range(1,13):
        print(f"{num} x {i} = {num*i}")
tabla_de_multiplicar(numero)    