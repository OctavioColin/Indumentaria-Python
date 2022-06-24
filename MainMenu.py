from Query import QueryIndumentaria
#Main
option = 10
while(option != 0):
    print("----Menu De Opciones----")
    print("[1] Consulta de Ropa.")
    print("[2] Consulta de Accesorios.")
    print("[3] Consulta de Calzado.")
    print("[0] Salir.")
    try:
        option = int(input("-->"))
        if(option == 1):
            QueryIndumentaria.queryRopa()
        elif(option == 2):
            QueryIndumentaria.queryAccesorios()
        elif(option == 3):
            QueryIndumentaria.queryCalzado()
        elif(option == 0):
            print("Fin del programa. Gracias")
            break
        else:
            print("Opción no válida.")
    except Exception:
        print("Entrada invalida.")


