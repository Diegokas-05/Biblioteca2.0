from exceptions import LibroNoEncontradoError, UsuarioNoEncontradoError
from libros import LibroFisico, libroDigital
from usuarios import Estudiante, Profesor


class Biblioteca:
    def __init__(self, nombre):
        self.nombre = nombre
        self.libros = [] # aqui se guardaran los libros que tenga la biblioteca
        self.usuarios = [] # aqui se guardaran los usuarios que tenga la biblioteca

    #metodo para meter un libro ala lista de biblioteca
    def registrar_libro(self, libro):
        self.libros.append(libro)
        return f"El libro {libro.titulo} ha sido registrado en {self.nombre}."

    #metodo para registrar un usuario en la biblioteca
    def registrar_usuario(self, usuario):
        self.usuarios.append(usuario)
        return f"El usuario {usuario.nombre} ya es miembro de la biblioteca."

    #metodo para bucar un usuario por su cedula
    def buscar_usuario(self, cedula):
        #recorremos la lista de usuarios y comparamos la cedula que nos pasan con la cedula de cada usuario
        for usuario in self.usuarios:
            if usuario.cedula == cedula:
                return usuario # si encontramos el usuario lo retornamos completo el usuario

        raise UsuarioNoEncontradoError(f"El usuario con cédula {cedula} no está registrado.")

    #Metodo para buscar libros por su titulo
    def buscar_libro(self, titulo):
        for libro in self.libros:
            if libro.titulo ==titulo and libro.disponible == True: #comparamos el titulo que nos pasan con el titulo de cada libro y ademas verificamos que este disponible
                return libro 
            
        raise LibroNoEncontradoError(f"El libro con título {titulo} no está disponible.")

    def realizar_prestamo(self, cedula_usuario, titulo_libro):
        # Si las búsquedas fallan, el código se detendrá aquí mismo y lanzará el error.
        usuario_encontrado = self.buscar_usuario(cedula_usuario)
        libro_encontrado = self.buscar_libro(titulo_libro)

        # Si llegamos a esta línea, significa que ambos existen y no hubo errores.
        mensaje = libro_encontrado.prestar()
        usuario_encontrado.libros_prestados.append(libro_encontrado.titulo)

        return f"Éxito: {mensaje} Entregado a {usuario_encontrado.nombre}."
    
