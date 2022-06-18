#ejercicio de crear un factorial a un numero
#el factorial no se puede realizar con numero negativos

numero = int(input("Ingrese el numero: "))
while numero < 0:#Mientras el numero sea negativo se repetira
    print("Error el numero tiene que ser positivo")
    numero = int(input("Ingrese el numero: "))

mult = 1
for i in range(1,numero+1):
    mult *= i 
    print(f"cuando i sea {i} ---> entonces mult sera {mult}")
    
print(mult)