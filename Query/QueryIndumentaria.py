import mysql.connector

from Query.Connector import get_conexion
from Util.FilesIndumentaria import guardaRopa, guardaAccesorios, guardaCalzado

def queryRopa():
    try:
        conexion = get_conexion()
        ropa = []
        with conexion.cursor() as cursor:
            cursor.execute("select articulos.id, articulos_ropa_detalles.* " +\
                           " from articulos " +\
                           " join articulos_ropa_detalles " +\
                           " on articulos.id = articulos_ropa_detalles.idArticulo")
            ropa = cursor.fetchall()
        for prenda in ropa:
            linea = "------------------------------------------------\n" +\
                    "  Articulos.id: " + str(prenda[0]) + "\n" + \
                    "  id: " + str(prenda[1]) + "\n" + \
                    "  idArticulo: " + str(prenda[2]) + "\n" + \
                    "  tipo: " + prenda[3] + "\n" + \
                    "  usabilidad: " + prenda[4] + "\n" + \
                    "  talle: " + prenda[5] + "\n" + \
                    "  temporada: " + prenda[6] + "\n" + \
                    "  Color: " + prenda[7] + "\n" + \
                    "------------------------------------------------\n"
            print(linea)
        guardaRopa(ropa)
        conexion.close()
    except mysql.connector.Error as err:
        print("Error en consulta de Ropa. {}".format(err))

def queryAccesorios():
    try:
        conexion = get_conexion()
        accesorios = []
        with conexion.cursor() as cursor:
            cursor.execute("select articulos.id, articulos_accesorios_detalles.* from articulos " +\
                           " join articulos_accesorios_detalles " + \
                           " on articulos.id = articulos_accesorios_detalles.idArticulo")
            accesorios = cursor.fetchall()
        for accesorio in accesorios:
            linea = "------------------------------------------------\n" + \
                    "  Articulos.id: " + str(accesorio[0]) + "\n" + \
                    "  id: " + str(accesorio[1]) + "\n" + \
                    "  idArticulo: " + str(accesorio[2]) + "\n" + \
                    "  tipo: " + accesorio[3] + "\n" + \
                    "  color: " + accesorio[4] + "\n" + \
                    "------------------------------------------------\n"
            print(linea)
        guardaAccesorios(accesorios)
        conexion.close()
    except mysql.connector.Error as err:
        print("Error en consulta de Accesorios. {}".format(err))

def queryCalzado():
    try:
        conexion = get_conexion()
        calzado = []
        with conexion.cursor() as cursor:
            cursor.execute("select articulos.id, articulos_calzados_detalles.* from articulos " +\
                           " join articulos_calzados_detalles " +\
                           " on articulos.id = articulos_calzados_detalles.idArticulo ")
            calzado = cursor.fetchall()
        for par in calzado:
            linea = "------------------------------------------------\n" + \
                    "  Articulos.id: " + str(par[0]) + "\n" + \
                    "  id: " + str(par[1]) + "\n" + \
                    "  idArticulo: " + str(par[2]) + "\n" + \
                    "  tipo: " + par[3] + "\n" + \
                    "  usabilidad: " + par[4] + "\n" + \
                    "  numero: " + str(par[5]) + "\n" + \
                    "  color: " + par[6] + "\n" + \
                    "------------------------------------------------\n"
            print(linea)
        guardaCalzado(calzado)
        conexion.close()
    except mysql.connector.Error as err:
        print("Error en consulta de Calzado. {}".format(err))