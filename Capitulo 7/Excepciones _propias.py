


def verificando_edad(edad):
    if edad < 0:
        raise ValueError ("La edad no puede ser negativa")#asi se crea nuestra propia excepcion con raise
    elif edad < 18:
        print("Eres menor de edad")
    
edad = int (input("Ingrese su edad: "))
try:
    verificando_edad(edad)
except ValueError as edadnegativa:
         print(edadnegativa)
