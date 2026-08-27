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


# 1. Creamos nuestra Biblioteca
mi_biblio = Biblioteca("Biblioteca Central")

# 2. Fabricamos un libro y un estudiante usando las clases que IMPORTAMOS arriba
nuevo_libro = LibroFisico("Cien Años de Soledad", "Gabriel García Márquez", "123")
nuevo_estudiante = Estudiante("Juan", "001", "Ingeniería")

# 3. Metemos el libro y el estudiante dentro de la biblioteca
mensaje_libro = mi_biblio.registrar_libro(nuevo_libro)
mensaje_usuario = mi_biblio.registrar_usuario(nuevo_estudiante)

print(mensaje_libro)
print(mensaje_usuario)

# 4. Verificamos que realmente están guardados en las listas
print(f"Total de libros guardados: {len(mi_biblio.libros)}")
print(f"Total de usuarios guardados: {len(mi_biblio.usuarios)}")