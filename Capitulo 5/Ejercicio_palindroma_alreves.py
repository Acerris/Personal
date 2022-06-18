
frase= input("Introduzca una frase: ")
#primero quitamos los espacios en blanco de la cadena
frase = frase.replace(" ","")

frase2 = frase[::-1]
print(f"Primera cadena:{frase}, al reves {frase2}")
if frase == frase2:
    print("La frase o palabra es palindroma")
else:
    print("No es palindroma")