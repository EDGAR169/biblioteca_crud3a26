class Libro:


    def __init__(self,id,titulo,autor,isbn,disponible):
        self.id = id 
        self.titulo = titulo
        self.autor = autor
        self.isbn = isbn
        self.disponible = disponible

    def prestar(self):
        if self.disponible:
            self.disponible = True 
            return False 

    def devolver (self):
        self.disponible = True     

    def mostrar_info(self):
        return f"Libro ID: {self.id_libro},Titulo:{self.titulo},Autor:{self.autor},isbn{self.isbn} "     