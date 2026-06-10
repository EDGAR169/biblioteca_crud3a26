from models.libro import libro

class prestamo:

    #Constructor
    def ___init__(self,id_prestamo,usuario,libro,fecha_prestamo,fecha_devolucion):
        self.id_prestamo = id_prestamo
        self.usuario = usuario
        self.libro = libro
        self.fecha_prestamo = fecha_prestamo
        self.fecha_devolucion = fecha_devolucion
        self.devuelte = False

    def registrar_devolucion(self):
        self.devuelto = True
        self.libro.devolver()

    def mostrar_info(self):
        return f"Prestamo ID: {self.id_prestamo},usuario: {self.usuario.nombre},Libro: {self.libro.titulo},Fecha_prestamo: {self.fecha_prestamo}, fecha_devolucion:{self.fecha_devolucion},Devolucion: {'si' if self.devolucion else 'No'}"        

