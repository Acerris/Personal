
from traceback import print_tb


def sumar_digitos(num):
    if num == 0:
        resultado = 0
    else:
        resultado = sumar_digitos(int(num/10)) + (num%10)
        print(resultado)

    return resultado

print(sumar_digitos(123))