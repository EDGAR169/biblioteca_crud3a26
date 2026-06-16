from dao.libro_dao import LibroDAO
from models.libro import Libro

def main(): 
    try:
        libro_dao = LibroDAO()#tIENE TODS LOS LIBRS DE DAO

        libros = libro_dao.obtener_todos()

        print("=== Libros en biblioteca ===")

        if len(libro)== 0:
            prin("No hay libros.")

        else:
            for libro in libros:
                print("=================")
                print(
                f"ID:{libro.id}, Titulo:{liro.titulo},"
                f"Autor: {libro.autor}, ISBN: {libro.isbn},"
                f"Disponible: {'si'if libro.disponible else 'NO'}"
                )
                print("===================")
        print("\n conexion exitosa a la base de datos")        
    except Exception as e:
        print("Error:")
        print (e)

if __name__ == "__main__":
    main()            