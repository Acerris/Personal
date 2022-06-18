def cambio_de_soles_a_dolares(soles):
    return soles/3.3
def cambio_de_dolares_a_soles(dolares):
    return dolares*3.3
while True:
    print(""".:Menu:.
1.Convertir Soles a Dolaress
2.Convertir Dolares a Soles
3.salir
""")
    opcion = input("Elija una opcion: ")
    print()

    if opcion == "1":
        soles = float(input("Ingrese la cantidad de soles: "))
        print(f"dolares ---> ${cambio_de_soles_a_dolares(soles):.2f}")
    
    elif opcion == "2":
        dolares = float(input("Ingrese la cantidad de dolares: "))
        print(f"soles ---> ${cambio_de_dolares_a_soles(dolares):.2f}")
    
    elif opcion == "3":
        break

    else:
        print("Se equivoco de opcion")