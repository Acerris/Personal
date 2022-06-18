#primera forma de hacerlo
"""
palabra1 = input("Ingrese la primera Palabra: ")
palabra2 = input("Ingrese la segunda Palabra: ")

numpalabra1=(len(palabra1))
numpalabra2=(len(palabra2))

if numpalabra2>numpalabra1:
    print("La palabra con mas caracteres es: ",palabra2)

elif numpalabra1>numpalabra2:
    print("La palabra con mas caracteres es: ",palabra1)

else:
    print("Son iguales") 
"""

#segunda forma
palabra1 = input("Ingrese la primera Palabra: ")
palabra2 = input("Ingrese la segunda Palabra: ")

if len(palabra2)>len(palabra1):
    print("La palabra con mas caracteres es: ",palabra2)

elif len(palabra1)>len(palabra2):
    print("La palabra con mas caracteres es: ",palabra1)

else:
    print("Son iguales")