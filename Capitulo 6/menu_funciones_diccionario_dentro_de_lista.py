
def agregar_cliente(clientes,nombre,apellido,dni): #Creamos la funcion agregar clientes,le indicamos los parametros
    cliente = {} #Creamos un Diccionario
    cliente ["nombre"] = nombre
    cliente ["apellido"] = apellido
    cliente ["dni"] = dni
    clientes.append(cliente)
#En  la funcion agregar clientes estamos guardando un diccionario dentro de una lista

def mostrar_clientes(clientes):
    for i in clientes:
        print(f"Nombre: {i['nombre']}, Apellido: {i['apellido']}, DNI {i['dni']}")

def mostrar_cliente_dni(clientes,dni):
    for i in clientes:
        if i['dni'] == dni:
            print(f"Nombre: {i['nombre']}, Apellido: {i['apellido']}, DNI {i['dni']}")
            return True
    return False

def eliminar_cliente(clientes,dni):
    for i in clientes:
        if i['dni'] == dni:
            clientes.remove(i)
            return True
    return False
clientes = [] #creamos una lista

while True:
    print("""\t.:Menu:.
    1.Agregar nuevo cliente
    2.Mostrar todos los clientes
    3.Mostrar cliente por DNI
    4.Eliminar cliente
    5.salir""")

    opcion = input("Ingrese una opcion: ")

    if opcion == "1":
        nombre = input("Ingrese el nombre del cliente: ")
        apellido = input("Ingrese el apellido del cliente: ")
        dni = input("Ingrese el DNI del cliente: ")
        agregar_cliente(clientes,nombre,apellido,dni)

    elif opcion == "2":
        mostrar_clientes(clientes)
    
    elif opcion == "3":
        dni = input("Ingrese el DNI del cliente: ")
        if mostrar_cliente_dni(clientes,dni):
            print("Cliente Encontrado")
        else:
            print("Cliente no encontrado")
    
    elif opcion == "4":
        dni = input("Ingrese el DNI del cliente: ")
        if eliminar_cliente(clientes,dni):
            print("Cliente eliminado")
        else:
            print("Cliente no encontrado")
    
    elif opcion == "5":
        break

    else:
        print("Se equivoco de opcion")