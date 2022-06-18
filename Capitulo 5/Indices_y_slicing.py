#lAS CADENAS DE CARACTERES SON INMUTABLES
cadena = "Fermin"

print(cadena[0])

#Slicing
print(cadena[0:3])
print(cadena[2:])

#realizar cambio de mayuscula a minuscula
cadena = "Angela Aguilar"
cadena = 'a' + cadena[1:]
print(cadena)

print(cadena.upper())#pondra en mayuscula todas las letras
print(cadena.lower())#pondra todas las letras en minuscula
print(cadena.capitalize())#Pondra en mayuscula la primera palabra que encuentre
print(cadena.title())#Esta convertira en mayuscula cada primera letra de cada palabra
print(cadena.count('u'))#esto retorna cuantas veces sale la letra a
print(cadena.find('a'))#busca la primera letra o palabra que encuentre y te muestra el indice en el que se encuentra
print(cadena.rfind('a'))#busca la ultima coincidencia, significa r de reverse find
print("12".isdigit())#Indica si el valor es un digito, tirara True o false
print(cadena.isalpha())#valida si es una palabra o no, no acepta caracteres especiales
print(cadena.isalnum())#Valida si nuestra cadena es alphanumerica,no acepta caracteres especiales
print(cadena.islower())#valida si la cadena es minuscula,siempre y cuando todo este minuscula
print(cadena.isupper())#valida si la cadena es mayuscula,siempre y cuando sea todo mayuscula
print(cadena.istitle())#valida si es un titulo
print(cadena.isspace())#valida si toda la cadena esta compuesta de espacios
cadena = "Angela"
print(cadena.startswith('A'))#valida si la primera letra de la cadena es a o tambien se puede usar con palabras
print(cadena.endswith('a'))#valida si la ultima letra de la cadena es a
cadena = "Angela Aguilar Dominguez".split()#Agarra la cadena y cada vez que vea un espacio y me retornara una lista
print(cadena)
cadena = "Angela-Aguilar-Dominguez".split('-')#Agarra la cadena y cada vez que vea un - y los separara y me retornara una lista
print(cadena)
cadena = ",".join("Fermin")#me separa cada caracter con una coma, tambien se puede hacer con puntos u otro caracter
print(cadena)

cadena= "      Hola      ".strip()#al estar el strip vacio elimina todos los espacios y solo deja la palabra
print(cadena)
cadena= "......Hola.....".strip('.')#elimina todos los puntos de la cadena
print(cadena)

cadena = "Hola Mundo".replace('o','0')#Reemplaza todas las o por un 0
print(cadena)
cadena = "Hola Mundo".replace('Hola','HOLA')
print(cadena)


