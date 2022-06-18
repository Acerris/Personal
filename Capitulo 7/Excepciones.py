while True:
    try:#Aqui intentara realizar el codigo  que coloque el usuario
        numero = int(input("Ingrese un numero: "))
        print(numero+10)

    except:#aqui capturara la excepcion osea el error, en caso de que trate de sumar un string
        print("Error coloque el numero entero")
    
    else:#es el caso contrario del except 
        print("el else: Programa finalizado")
        break

    finally:#el se ejcutara siempre, con el try y el except
        print("el finally: funciono")
    #el finally se usa para base de datos, la conexion siempre necesitara cerrarse para este caso funcionaria
    