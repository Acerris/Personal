#tabla de multiplicar hasta el 10

numero = int(input("Ingrese el numero: "))
while numero < 0:#Mientras el numero sea negativo se repetira
    print("Error el numero tiene que ser positivo")
    numero = int(input("Ingrese el numero: "))

lista = []

for i in range(1,10+1):
    multiplicacion = i * numero
    lista.append(multiplicacion)

print(lista)