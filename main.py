from biblioteca import Biblioteca

# Asegúrate de usar los nombres exactos que tú creaste
from exceptions import LibroNoEncontradoError, UsuarioNoEncontradoError
from libros import LibroFisico
from persistencia import Persistencia
from usuarios import Estudiante

print("Iniciando el sistema de la biblioteca...")

# 1. Preparamos nuestra biblioteca con datos iniciales
#mi_biblio = Biblioteca("Biblioteca Central") ###Ya no usamos eso por que hora el nombre de la biblioteca se carga desde el archivo JSON

# Preparamos nuestra herramienta de guardado
guardador = Persistencia()

# Intentamos cargar los datos desde el archivo JSON
mi_biblio = guardador.cargar_datos()

# Si no hay datos previos, creamos una nueva biblioteca y agregamos algunos libros y usuarios de ejemplo
if mi_biblio is None:
    print("No se enocontron datos previos. Creando una nueva biblioteca...")
    mi_biblio = Biblioteca("Biblioteca Central")
    mi_biblio.registrar_libro(LibroFisico("Monster", "Frank Peretti", "9781"))
    mi_biblio.registrar_libro(LibroFisico("El Principito", "Antoine de Saint-Exupéry", "9782"))
    mi_biblio.registrar_usuario(Estudiante("Diego Aaron", "123", "Ingeniería"))
else:
    print(f"Base de datos cargada con exito: {len(mi_biblio.libros)} libros encontrados")

print(f"--- Bienvenido al sistema de la {mi_biblio.nombre} ---")

# 2. El ciclo infinito del menú
while True:
    print("\n¿Qué deseas hacer?")
    print("1. Ver cantidad de libros registrados")
    print("2. Solicitar un libro")
    print("3. Salir")

    # input() pausa el programa y espera a que el usuario escriba algo
    opcion = input("Digita el número de tu opción: ")
    
    # `match` es una nueva forma de hacer condicionales en Python
    match opcion:
        case "1":
            print(f"\n[INFO] Actualmente tenemos {len(mi_biblio.libros)} libros en el sistema.")

        case "2":
            print("\n--- Solicitar un libro ---")
            cedula_ingresada = input("Ingresa tu cédula: ")
            titulo_ingresado = input("Ingresa el título del libro que deseas: ")
            
            # Le decimos a Python: "INTENTA ejecutar este código que es peligroso"
            try:
                resultado_prestamo = mi_biblio.realizar_prestamo(cedula_ingresada, titulo_ingresado)
                # Si todo sale bien, imprimimos el éxito
                print(f"\n✅ {resultado_prestamo}")
                
            # Si la biblioteca grita el error del libro, lo ATRAPAMOS aquí:
            except LibroNoEncontradoError as e:
                # La 'e' guarda el mensaje que le mandamos desde biblioteca.py
                print(f"\n❌ [ERROR DE LIBRO]: {e}")
                
            # Si la biblioteca grita el error del usuario, lo ATRAPAMOS aquí:
            except UsuarioNoEncontradoError as e:
                print(f"\n❌ [ERROR DE USUARIO]: {e}")

        case "3":
            print("\nGuardando datos antes de salir...")
            guardador.guardar_datos(mi_biblio)
            print("\nSaliendo del sistema... ¡Hasta pronto!")
            break  # La palabra 'break' destruye el ciclo while y termina el programa
        case _:    # El guion bajo (_) significa "cualquier otra cosa que no sea 1, 2 o 3"
            print("\n[ERROR] Opción no válida. Por favor digita 1, 2 o 3.")