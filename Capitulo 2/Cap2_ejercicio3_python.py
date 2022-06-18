#Realizar un programa que indique si el caracter es una vocal o no

#la funcion .lower() al final de la linea hace que todo caracter que ingresen en mayuscula se convierta a minuscula
letra = input("Ingrese una letra: ").lower()
#podemos escribir tambien si no lo queremos colocar en esa linea 
#letra = letra.lower() -- hay que recordar que lower te guarda una COPIA de lo ingresado pero te lo convierte a minuscula
if letra == "a" or letra == "e" or letra == "i" or letra == "o" or letra== "u":
    print("  es una vocal")

else:
    print(" no es una vocal")

#tambien existe upper() para convertirlo a mayuscula