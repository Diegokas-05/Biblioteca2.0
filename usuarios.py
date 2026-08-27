class Usuarios:
    def __init__(self, nombre, cedula):
        self.nombre = nombre
        self.cedula = cedula
        #intrudicmo una lista vacia para que los usuarios puedan tener libros prestados
        self.libros_prestados = []


class Estudiante(Usuarios):
    def __init__(self, nombre, cedula, carrera):
        #la clase super nos permite llamar a la clase padre y heredar sus atributos y metodos
        super().__init__(nombre, cedula)
        # dato exclusivo de la clase estudiante
        self.carrera = carrera
        self.limite_libros = 3 #limite de libros para el estudiante

class Profesor(Usuarios):
    def __init__(self, nombre, cedula):
        super().__init__(nombre, cedula)
        self.limite_libros = None #no hay limite de libros para el profesor
