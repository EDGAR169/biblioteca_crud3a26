from dao.libro_dao import LibroDAO
from models.libro import Libro

def  ver_libros():


    try:
        libro_dao = LibroDAO()#tIENE TODS LOS LIBRS DE DAO

        libros = libro_dao.obtener_todos()

        print("=== Libros en biblioteca ===")

        if len(libros)== 0:
            prin("No hay libros.")

        else:
            for libro in libros:
                print("=================")
                print(
                f"ID:{libro.id}, Titulo:{libro.titulo},"
                f"Autor: {libro.autor}, ISBN: {libro.isbn},"
                f"Disponible: {'si'if libro.disponible else 'NO'}"
                )
                print("===================")
        print("\n conexion exitosa a la base de datos")        
    except Exception as e:
        print("Error:")
        print (e)


def insertar_libro():
    tiulo= imput("Escribe el titulo del nuevo libro:")
    autor = int (input("Escribe el id del autor:"))
    isbn = input("Escribe el isbn del nuevo libro:")
    disponible = True
    try:
        libro_dao = LibroDAO()
        id = libro_dao.obtener_ultimo_id()+ 1
        libro = Libro(id,titulo,autor,isbm,disponible)
        libro_dao.insert(libro)
        print("Inserción realizada con éxito")
    except Exeption as e:
        print("Error al insertar nuevo libro")
        print(e)

def main():
    print("===BIBLIOTECA UNIVERSAL===")
    print("Menú de opciones")
    print("1. Ver todos los libros")
    print("2. insertar un nuevo libro")
    print("3. Actualizar un libro disponible")
    print("4. Elimina un libro disponible")   
    opcion = int (input("Selecciona una opcion (1-4):"))

    match opcion: 
        case 1:
            ver_libros()
        case 2:
            insertar_libros()
        case 3: 
            actualizar_libro()
        case 4: 
            eliminar_libro()

    

if __name__ == "__main__":
    main()            