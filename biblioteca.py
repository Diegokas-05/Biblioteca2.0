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

        return None # si termina el ciclo y no encuentra el usuario retornamos None

    #Metodo para buscar libros por su titulo
    def buscar_libro(self, titulo):
        for libro in self.libros:
            if libro.titulo ==titulo and libro.disponible == True: #comparamos el titulo que nos pasan con el titulo de cada libro y ademas verificamos que este disponible
                return libro 
            
        return None

    def realizar_prestamo(self, cedula_usuario, titulo_libros):
        #usamos nuestros propios metodo para buscar
        usuario_encontrado = self.buscar_usuario(cedula_usuario)
        libro_encontrado = self.buscar_libro(titulo_libros)

        if usuario_encontrado == None:
            return "Error: El usuario no esta registrado"

        if libro_encontrado == None:
            return "Error: El libro no esta disponible"

        mensaje = libro_encontrado.prestar()

        usuario_encontrado.libros_prestados.append(libro_encontrado.titulo)

        return f"Exito: {mensaje} Entregado a {usuario_encontrado.nombre}."

    
# 1. Preparamos todo
biblio = Biblioteca("Mi Biblioteca")
biblio.registrar_libro(LibroFisico("Monster", "Frank Peretti", "9781"))
biblio.registrar_usuario(Estudiante("Diego Aaron", "123", "Ingeniería"))

# 2. Hacemos el préstamo
resultado = biblio.realizar_prestamo("123", "Monster")
print(resultado)

# 3. Intentamos prestar el mismo libro a otra persona que no existe
resultado_malo = biblio.realizar_prestamo("999", "Monster")
print(resultado_malo)