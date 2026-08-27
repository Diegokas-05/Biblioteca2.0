
class Libro:
    def __init__(self,titulo, autor, isbn):
        #aqui definimos lo que mis libros van a tener como atributos
        self.titulo = titulo
        self.autor = autor
        self.isbn = isbn
        self.disponible = True

    #metodo para prestar el libro
    def prestar(self):
        if self.disponible == True: #vemos que el libro este disponible para prestar
            self.disponible = False #marcamos false por que el libro ya no esta disponible
            return f"el libro {self.titulo} ha sido prestado exitosamente"
        else:
            return f"El libro {self.titulo} no esta disponible para prestar"
    # metodo para devolver el libro
    def devolver(self):
        if self.disponible == False:
            self.disponible = True
            return f"El libro {self.titulo} ha sido devuelto exitosamente"

#Hacemo que los libros fisico y digitales herede de libros poniendole entre parentesis el nombre de la clase padre 
#esto es el polimorfismo, ya que los metodos de la clase padre se pueden usar en las clases hijas
class LibroFisico(Libro):
    def calcular_duracion(self):
        return "El prestamo dura 7 dias"

class libroDigital(Libro):
    def calcular_duraacion(self):
        return "El prestamo dura 14 dias"

