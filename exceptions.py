class BibliotecaError(Exception):
    """Clase base para errores relacionados con la biblioteca."""
    pass

class UsuarioNoEncontradoError(BibliotecaError):
    """Excepción lanzada cuando un usuario no se encuentra en la biblioteca."""
    pass

class LibroNoEncontradoError(BibliotecaError):
    """Excepción lanzada cuando un libro no se encuentra en la biblioteca."""
    pass