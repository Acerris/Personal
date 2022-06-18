Agenda = {} #Diccionario vacio

while True:
    print("\n1. Nuevo contacto \n2.Borrar Contacto \n3.Ver contactos existentes \n4.Salir")
    opcion = input("Ingrese la opcion: ")

    if opcion == '1':
        nombre = input("Ingrese el nombre del contacto: ")
        telefono = input("Ingrese el numero telefonico: ")

        if nombre not in Agenda:
            Agenda[nombre] = telefono
            print("\nContacto agregado\n")
        else:
            print("\nEl nombre del contacto ya existe.\n")
    
    elif opcion == '2':
        borrar = input("Ingrese el contacto que desea eliminar: ")
        if borrar not in Agenda:
            print("Este contacto no existe")
        else:
            del(Agenda[borrar])
            print("\nContacto Eliminado\n")
    
    elif opcion == '3':
        for clave,valor in Agenda.items():
            print(f"Nombre: {clave}, telefono: {valor}")
    
    elif opcion == '4':
        break

    else:
        print("Elija una opcion correcta")