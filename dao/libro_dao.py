#DAO: DATA ACCESS OBJECT
#Libro_dao: Objeto de acccesoa datos de la tablalibro

from database.conexion import Conexion
from models.libro import Libro

class LibroDAO:

    def obtener_todos (self):
        conexion = Conexion.obtener_conexion()#SEECT * FROM libro
        cursor = conexion.cursor()#Objeto para sql

        cursor.execute("SELECT * FROM libro")
        registros = curson.fetchall()

        libros = []
        for registro in registros:
            libro = Libro (registro.id,
            registro.titulo,
            registro.autor,
            registro.isbn,
            registro.disponible)
            libros.append(libro)
        cursor.close()
        conexion.close()
        return libros

    def insetar (self,libro):  
        conexion = Conexion.obtener_conexion()
        cursor = conexion.cursor()
        sql = """
        INSERT INTO libro( titulo,autor,ibn,disponible)
        VALUES (%s,%s,%s,%s)
        """
        #Los vaores que se pongam encursor seran iguales a los parametros que ingresamo
        cursor.execute(
            sql,
            (libro.titulo,
            libro.autor,
            libro.isbn,
            libro.disponible)
        )

        conexion.commit()
        cursor .close()
        conexion.close()

    def actualizar (self,libro):
        conexion = conexion.obtener_conexion()
        cursor = conexion.cursor()
        sql = """
        UPDAT libro
        SET titulo = %s, autor = %s, isbn = %s, disponible = %s
        WHERE id = %s
        """
        #ID en where sirbe olo para saber que libro es el que se modifica
        #IMPORTANCIA EN E ORDEN QUE SEAGREGO
        curso.execute(
            sql,
            (libro.titlo,
            libro.autor,
            libro.isbn,
            libro.disponible,
            lbro.id)
        )
        conexion.commit()
        cursor.close()
        conexion.close()

    def eliminar (self,liro_id):
        conexion = conexion.obtenr_conxion()
        cursor = conexion.cursor()

        cursor.execute("DELETE FROM libroid = %s",
        (libro_id,))

        conxion.commit()
        cursor.close()
        conexion.close()




