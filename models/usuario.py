class Usuario:

    #contructor
    def __init__(self,id,nombre,matricula,carrera,correo):# corregido:id_usuario por id
        self.id = id # Tambien
        self.nombre = nombre 
        self.matricula = matricula

        self.carrera = carrera
        self.correo = correo
        self.activo = True
    
    def activar(self):
        self.activo = True

    

    def desactivar(self):
        self.activo = False

    def mostrar_info(self):
        return f"Usuario ID: {self.id}, Nombre: {self.nombre}, Matricula:{self.matricula} Correo: {self.correo},Carrera:{self.carrera},Activo: {'si'if self.activo else 'No'}"    #lo mismo del id