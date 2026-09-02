# Importamos la librería json que ya viene instalada en Python
import json

from biblioteca import Biblioteca
from libros import LibroFisico
from usuarios import Estudiante


class Persistencia:
    def __init__(self, archivo="biblioteca.json"):
        # Le decimos cómo se va a llamar el archivo donde guardaremos todo
        self.archivo = archivo

    def guardar_datos(self, biblioteca):
        # El truco mágico: __dict__
        # Python no sabe cómo guardar un objeto "Libro" directamente en texto.
        # Al usar __dict__, convertimos las características del libro en un diccionario (texto).
        
        datos = {
            "nombre": biblioteca.nombre,
            "usuarios": [usuario.__dict__ for usuario in biblioteca.usuarios],
            "libros": [libro.__dict__ for libro in biblioteca.libros]
        }
        
        # 'w' significa Write (escribir). Esto crea el archivo o lo sobreescribe.
        with open(self.archivo, "w", encoding="utf-8") as f:
            # json.dump toma nuestros datos y los escribe en el archivo con formato bonito (indent=4)
            json.dump(datos, f, ensure_ascii=False, indent=4)

    def cargar_datos(self):
            try:
                # Abrimos el archivo en modo lectura ('r') y le decimos que use UTF-8 para caracteres especiales
                with open(self.archivo, "r", encoding="utf-8") as f:
                    # Leemos el contenido del archivo y lo convertimos de JSON a un diccionario de Python
                    datos_leidos = json.load(f)
                # Creamos una nueva instancia de Biblioteca usando el nombre que leímos del archivo
                biblioteca_recuperada = Biblioteca(datos_leidos["nombre"])

                # Ahora vamos a reconstruir los libros y usuarios desde los diccionarios que leímos
                for dict_libro in datos_leidos["libros"]:
                    # Creamos un nuevo libro físico usando los datos del diccionario
                    nuevo_libro = LibroFisico(dict_libro["titulo"], dict_libro["autor"], dict_libro["isbn"])
                    # Restauramos el estado de disponibilidad del libro desde el diccionario
                    nuevo_libro.disponible = dict_libro["disponible"]
                    # Agregamos el libro a la lista de libros de la biblioteca recuperada
                    biblioteca_recuperada.libros.append(nuevo_libro)

                # Ahora hacemos lo mismo para los usuarios
                for dict_usuario in datos_leidos["usuarios"]:
                    # Creamos un nuevo usuario estudiante usando los datos del diccionario
                    nuevo_usuario = Estudiante(dict_usuario["nombre"], dict_usuario["cedula"], dict_usuario["carrera"])
                    # Restauramos la lista de libros prestados del usuario desde el diccionario
                    nuevo_usuario.libros_prestados = dict_usuario["libros_prestados"]
                    # Agregamos el usuario a la lista de usuarios de la biblioteca recuperada
                    biblioteca_recuperada.usuarios.append(nuevo_usuario)
                # Devolvemos la biblioteca reconstruida con todos sus libros y usuarios
                return biblioteca_recuperada
            
            except FileNotFoundError: # Si el archivo no existe, simplemente devolvemos None para indicar que no hay datos previos
                return None # Devolvemos None para indicar que no hay datos previos