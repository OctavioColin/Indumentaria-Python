def guardaRopa(ropa):
    try:
        archivo = open("Files/relaciones_de_tablas_Ropa_Articulos.txt", "w")
        for prenda in ropa:
            linea = str(prenda[0]) + "|" +\
                    str(prenda[1]) + "|" +\
                    str(prenda[2]) + "|" +\
                    prenda[3] + "|" +\
                    prenda[4] + "|" +\
                    prenda[5] + "|" +\
                    prenda[6] + "|" +\
                    prenda[7] + "\n"
            archivo.write(linea)
        archivo.close()
        print("Archivo \'relaciones_de_tablas_Ropa_Articulos.txt\' creado con éxito")
    except IOError as err:
        print("Error al generar archivo \'relaciones_de_tablas_Ropa_Articulos.txt\'. {}".format(err))

def guardaAccesorios(accesorios):
    try:
        archivo = open("Files/relaciones_de_tablas_Accesorios_Articulos.txt", "w")
        for accesorio in accesorios:
            linea = str(accesorio[0]) + "|" + \
                    str(accesorio[1]) + "|" + \
                    str(accesorio[2]) + "|" + \
                    accesorio[3] + "|" + \
                    accesorio[4] + "\n"
            archivo.write(linea)
        archivo.close()
        print("Archivo \'relaciones_de_tablas_Accesorios_Articulos.txt\' creado con éxito")
    except IOError as err:
        print("Error al generar archivo \'relaciones_de_tablas_Accesorios_Articulos.txt\'. {}".format(err))

def guardaCalzado(calzado):
    try:
        archivo = open("Files/relaciones_de_tablas_Calzado_Articulos.txt", "w")
        for par in calzado:
            linea = str(par[0]) + "|" + \
                    str(par[1]) + "|" + \
                    str(par[2]) + "|" + \
                    par[3] + "|" + \
                    par[4] + "|" + \
                    str(par[5]) + "|" + \
                    par[6] + "\n"
            archivo.write(linea)
        archivo.close()
        print("Archivo \'relaciones_de_tablas_Calzado_Articulos.txt\' creado con éxito")
    except IOError as err:
        print("Error al generar archivo \'relaciones_de_tablas_Calzado_Articulos.txt\'. {}".format(err))

