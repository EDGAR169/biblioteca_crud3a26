class Usuario:

    #contructor
    def __init__(self,id_usuario,nombre,email,carrera):
        self.id_usuario = id_usuario
        self.nombre = nombre 
        self.matricula = matricula
        self.email = email 
        self.carrera = carrera
        self.activo = True 
    
    def activar(self):
        self.avtivo = True

    

    def desactivar(self):
        self.ativo = False

    def mostrar_info(self):
        return f"Usuario ID: {self.id_usuario}, Nombre: {self.nombre}, Matricula:{self.matricula} Email: {self.email},Carrera:{self.carrera},Activo: {'si'if self.activo else 'No'}"    