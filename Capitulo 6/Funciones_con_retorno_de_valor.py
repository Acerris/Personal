#Funciones con retorno de valor

def multiplicar(num1,num2):
    mult = num1*num2
    return mult
mult=multiplicar(3,4)
print(mult)




#en python no solo puedes retornar un valor, si no varios valores
def prueba():
    return "Hola", 45, [1,2,3]
c,n,l = prueba()
print(c)
print(n)
print(l)