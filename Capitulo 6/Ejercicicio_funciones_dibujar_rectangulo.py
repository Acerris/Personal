def dibujar(ancho,alto):
    for i in range(alto):
        for j in range(ancho):
            print("* ",end="")
        print()

ancho=int(input("Ingrese el ancho: "))
alto=int(input("Ingrese el alto: "))

dibujar(ancho,alto)