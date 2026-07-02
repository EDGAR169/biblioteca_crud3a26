from dao.libro_dao import LibroDAO
from models.libro import Libro
#=======================================
from dao.usuario_dao import UsuarioDAO
from models.usuario import Usuario


def ver_usuarios():
    try:
        usuario_dao = UsuarioDAO()

        usuarios = usuario_dao.obtener_todos()

        print("===Usuarios existentes===")

        if len(usuarios)== 0:
            print("No hay usuarios.")

        else:
            for usuario in usuarios:
                print("==================")
                print(
                f"ID:{usuario.id},Nombre:{usuario.nombre},"
                f"Matricula:{usuario.matricula}, Correo:{usuario.correo},"
                f"Carrera: {usuario.carrera},Activo: {'Si'if usuario.activo else 'NO'}"  
                )
                print("===================")
        print("\n conexióna exiosa a la base de datos ")
    except Exception as e:
        print ("Error:")
        print (e)

def insertar_usuarios():
    nombre = input("Escribe el nombre del nuevo usuario:")
    matricula = input("Escrbe la matricula del usuario:")
    carrera = int(input("Escribe el id de la carrera:"))
    correo = input("Ecribe el correo electronico del usuario:")
    
    activo = True
    try:
        usuario_dao = UsuarioDAO()
        id = usuario_dao.obtener_ultimo_id() + 1
        usuario = Usuario (id,nombre,matricula,carrera,correo)
        usuario_dao.insertar(usuario)
        print("Inserción realizada con exito")
    except Exception as e:
        print("Error al insertar nuevo usuario")
        print (e)

def actualizar_usuarios():
    print ("Selccionar el usuario a actualizar")
    try:
        usuario_dao = UsuarioDAO()
        ver_usuarios()
        id = int (input("Escribe el id del usario a actualiza:"))
        nombre = input("Escribe  nuevo nombre de usuario:")
        matricula = input("Escrbe la nueva matricula:")
        correo = input("Ecribe el nuevo correo electronico:")
        carrera = int(input("Escribe el nuevo id de la carrera:"))
        activo = bool (input("Activo (si/no):"))#_----
        usuario = Usuario (id,nombre,matricula,carrera,correo)
        usuario_dao.actualizar (usuario)
        print (f"===El usuario-{id}- se ha actualizado correctamente===")
    except Exception as e:
        print ("Eror a actualizar usuario")
        print(e)

def eliminar_usuarios():
    try:
        usuario_dao = UsuarioDAO()
        print ("Lisa de usuarios disponibles:")
        ver_usuarios ()
        id = int(input("Escribe el usuario a eliminar:"))
        usuario_dao.eliminar(id)
        print(f"El usuario {id} ha sido eliminado con exito")
    except Exception as e:
        print("Error al eliminar usuario")
        print(e)


                
            

    


    

    


#=======================================
def  ver_libros():


    try:
        libro_dao = LibroDAO()#TIENE TODS LOS LIBRS DE DAO

        libros = libro_dao.obtener_todos()

        print("=== Libros en biblioteca ===")

        if len(libros)== 0:
            print("No hay libros.")

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
    titulo= input("Escribe el titulo del nuevo libro:")
    autor = int (input("Escribe el id del autor:"))
    isbn = input("Escribe el isbn del nuevo libro:")
    disponible = True
    try:
        libro_dao = LibroDAO()
        id = libro_dao.obtener_ultimo_id() + 1
        libro = Libro(id,titulo,autor,isbn,disponible)
        libro_dao.insertar(libro)
        print("Inserción realizada con éxito")
    except Exception as e:
        print("Error al insertar nuevo libro")
        print(e)

def actualizar_libro():
    print("Selecciona el libro a actualizar")
    try:
        libro_dao = LibroDAO()
        ver_libros()
        id = int (input("Escribe el id del libro a actualizar:"))
        titulo = input ("Escribe el nuevo titulo:")
        autor = input("Escribe el nuevo autor:")
        isbn = input ("Escribe el nuevo isbn:")
        disponible = bool (input("Escribe el nuevo valor de disponible:"))
        libro = Libro (id,titulo,autor,isbn,disponible)
        libro_dao.actualizar (libro)
        print(f"===El libro-{id}- se ha actualizado exitosamente===")
    except Exception as e:
        print("Error al actualizar un libro")
        print(e)

def eliminar_libro():
    try:
        libro_dao = LibroDAO()
        print ("Lista de libros disponibles:")
        ver_libros()
        id = int(input("Escribe el libro a eliminar:"))
        libro_dao.eliminar(id)
        print(f"El libro {id} ha sido eliminado con éxito")
    except  Exception as e:
        print(f"Error al eliminar el libro{id}")
        print (e)

def menu_libros():  
    print("1. Ver todos los libros")
    print("2. insertar un nuevo libro")
    print("3. Actualizar un libro disponible")
    print("4. Elimina un libro disponible")   
    opcion = int (input("Selecciona una opcion (1-4):"))

    match opcion: 
        case 1:
            ver_libros()
        case 2:
            insertar_libro()
        case 3: 
            actualizar_libro()
        case 4: 
            eliminar_libro()      

def menu_usuarios():  
    print("1. Ver todos los usuarios")
    print("2. insertar un nuevo usuario")
    print("3. Actualizar un usuario disponible")
    print("4. Elimina un usuario disponible")   
    opcion = int (input("Selecciona una opcion (1-4):"))

    match opcion: 
        case 1:
            ver_usuarios()
        case 2:
            insertar_usuarios()
        case 3: 
            actualizar_usuarios()
        case 4: 
            eliminar_usuarios()                  

def main():
    print("===BIBLIOTECA UNIVERSAL===")
    print("Menú de opciones")
    print("1. Gestión de libros")
    print("2. Gestionar usuarios")

    try:
        opcion = int(input("Selecciona una opcion genral (1-2)"))
        match opcion:
            case 1:
                 menu_libros()
            case 2:
                menu_usuarios()
            case 3: 
                print("opcion no valida.")

    except ValueError:
        print("porfaor introdusca un numero valido.")




        
            
    

    

if __name__ == "__main__":
    main()            