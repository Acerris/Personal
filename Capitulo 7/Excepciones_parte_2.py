# se pueden colocar una o mas excepciones
def dividir ():
    while True:
        try:#que intente ejecutar el codigo
            num1 = int(input("Digite un numero: "))
            num2 = int(input("Digite un numero: "))
            res = num1 /num2
            print("el resultado es: ",res)
    
        except ValueError:#se coloca el error value error que es cuando escriben un string en vez d eun numero entero
         print("error al ingresar string, coloque el numero")

        except ZeroDivisionError:#se colocar zero division cuando se divide entre 0
            print("No se puede dividir entre 0")
    
        else:#esto solo se coloca cuando esta en un while
            break

dividir()