import time as t
#las funciones recursivas son como bucles

def cuenta_regresiva(num): #aqui va el valor de 5
    if num > 0:# 5 es mayor a 0
        t.sleep(1)#que espere un segundo antes de imprimir
        print("\t",num,end="\r")#imprime el numero y el \r borra e imprime en esa misma linea
        cuenta_regresiva(num-1)#la funcion se llama a si misma con el valor de 5-1 = 4
    else:#si el numero es 0 o menor
        print("BOOOOOOOM!!!!")   #explota

cuenta_regresiva(5)#le asigno el valor de 5
