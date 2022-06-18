#realizar una cajero
saldo_inicial = 1000
while True:
    print("Elije una opcion: ")
    print("1.Ingresar dinero en la cuenta")
    print("2.retirar dinero de la cuenta")
    print("3.Mostrar dinero disponible")
    print("4.salir")
    opcion = int (input("Ingrese la opcion: "))

    if opcion == 1:
        massaldo = float(input("Ingrese la cantidad: "))
        saldo_inicial+=massaldo
        print(F"Su saldo es de: {saldo_inicial}\n")
    elif opcion == 2:
        menossaldo = float(input("Ingrese la cantidad: "))
        if menossaldo > saldo_inicial:
            print("No tiene suficientes fondos\n")
        else:
            saldo_inicial-= menossaldo
            print(f"su saldo es de {saldo_inicial}\n")

    elif opcion == 3:
        print(f"Su saldo es de {saldo_inicial}\n")

    elif opcion ==4:
        print("adios")
        break

    else:
        print("la opcion no existe\n")