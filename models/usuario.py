class Usuario:

    #Constructor
    def __init__(self, id, nombre. matricula, carrera, correo, activo):
        self.id = id
        self.nombre = nombre
        self.matricula = matricula
        self.carrera = carrera
        self.correo = correo
        self.activo = self.activo

    def activar(self):
        self.activo = True

    def desactivar(self):
        self.activo = False
    
    def mostrar_info(self):
        return f"ID Prestamo: {self.id_prestamo}, Nombre: {self.nombre}, Matricula: {self.matricula}, Carrera: {self.carerra.nombre_carrera}, Correo: {self.correo}, Activo {self.activo} "