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