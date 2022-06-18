#realizar una calculadora

print("Elije una opcion: ")
print("Suma --> presiona (S), (s)")
print("Resta --> presiona (R), (r)")
print("Multiplicacion -- > (P), (p), (M), (m)")
print("Division --> (D), (d)")
numero1 = float(input("Ingrese el primer numero: "))
numero2 = float(input("Ingrese el segundo numero: "))
opcion = input("Ingrese la opcion: ").lower()


if opcion == "s":
    print("La suma de los dos numeros es: ",numero1+numero2)

elif opcion == "r":
    print("La resta de los dos numeros es: ",numero1-numero2)

elif opcion == "p" or opcion =="m":
    print("La multiplicacion de los dos numeros es: ",numero1*numero2)

elif opcion == "d":
    print("La division de los dos numeros es: ",numero1/numero2)

else:
    print("La opcion ingresada no existe")