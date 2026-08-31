# Importamos la librería json que ya viene instalada en Python
import json


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