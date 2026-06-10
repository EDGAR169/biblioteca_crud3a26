class Libro:


    def __init__(self, id_libro,titulo,autor,isbn):
        self.id_libro = id_libro
        self.tiulo = titulo
        self.autor = autor
        self.isbn = isbn
        self.disponible = True

    def prestar(self):
        if self.disponible:
            self.disponible = True 
            return False 

    def devolver (self):
        self.disponible = True     

    def mostrar_info(self):
        return f"Libro ID: {self.od_libro},Titulo:{self.titulo},Autor:{self.autor},isbn{self.isbn} "     