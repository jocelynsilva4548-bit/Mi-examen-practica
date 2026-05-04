import sys
from servicios.catalogo import Catalogo
from modelos.libro import LibroFisico, LibroDigital
from modelos.usuario import Alumno, Profesor, Administrador

def seed_data(catalogo: Catalogo) -> None:
    """
    Inserta datos iniciales de prueba: 5 libros físicos, 5 digitales y usuarios.
    """
    # 1. Libros Físicos (5)
    catalogo.agregar_libro(LibroFisico("Don Quijote", "Cervantes", "9788437604947", 1605, "Clásico", "Estante A-1", 2))
    catalogo.agregar_libro(LibroFisico("Cien Años de Soledad", "G. Márquez", "9780307350435", 1967, "Literatura", "Estante A-2", 3))
    catalogo.agregar_libro(LibroFisico("El Principito", "Saint-Exupéry", "9780156013987", 1943, "Infantil", "Estante B-1", 5))
    catalogo.agregar_libro(LibroFisico("1984", "George Orwell", "9780451524935", 1949, "Distopía", "Estante C-1", 4))
    catalogo.agregar_libro(LibroFisico("Breve Historia del Tiempo", "S. Hawking", "9788432232305", 1988, "Ciencia", "Estante D-1", 1))
    
    # 2. Libros Digitales (5)
    catalogo.agregar_libro(LibroDigital("Aprende Python", "Guido", "9781111111111", 2022, "Tech", "PDF", 10.5, "http://python.org"))
    catalogo.agregar_libro(LibroDigital("Clean Code", "Robert Martin", "9780132350884", 2008, "Software", "EPUB", 5.2, "http://cleancode.com"))
    catalogo.agregar_libro(LibroDigital("El Hobbit", "J.R.R. Tolkien", "9780345339683", 1937, "Fantasía", "MOBI", 8.0, "http://hobbit.com"))
    catalogo.agregar_libro(LibroDigital("Inteligencia Artificial", "Russell", "9780136042594", 2009, "Ciencia", "PDF", 25.0, "http://ai.com"))
    catalogo.agregar_libro(LibroDigital("La Metamorfosis", "Franz Kafka", "9788420651361", 1915, "Ficción", "EPUB", 1.5, "http://kafka.com"))
    
    # 3. Usuarios de prueba
    u1 = Alumno("Jocelyn Silva", "jo@correo.com", "MAT-4548")
    u2 = Profesor("Dr. House", "house@correo.com", "Diagnóstico")
    catalogo.registrar_usuario(u1)
    catalogo.registrar_usuario(u2)
    
    print("\n[OK] El sistema ha sido cargado con 10 libros y usuarios de prueba.")


def main() -> None:
    """
    Función principal que orquesta el menú de consola y la persistencia de datos.
    """
    catalogo = Catalogo()
    
    # Carga inicial de datos desde archivo JSON
    try:
        catalogo.cargar_json("datos/biblioteca.json")
    except FileNotFoundError:
        print("\n>>> Bienvenido: No se encontró base de datos previa. Iniciando sistema limpio.")
    except Exception as e:
        print(f"\n>>> Error al cargar el archivo: {e}")

    while True:
        print("\n" + "="*45)
        print("  SISTEMA DE GESTIÓN DE BIBLIOTECA DIGITAL")
        print("="*45)
        print("1. Agregar Nuevo Libro")
        print("2. Buscar Libro (Título/Autor/ISBN)")
        print("3. Registrar Nuevo Usuario")
        print("4. Realizar Préstamo")
        print("5. Procesar Devolución")
        print("6. Ver Cola de Espera")
        print("7. Generar Reporte de Inventario")
        print("8. Cargar Datos de Ejemplo (Seed)")
        print("9. Guardar y Salir")
        print("-" * 45)
        
        opcion = input("Seleccione una opción (1-9): ")
        
        try:
            match opcion:
                case "1":
                    tipo = input("¿Tipo de libro? (F: Físico / D: Digital): ").upper()
                    titulo = input("Título: ")
                    autor = input("Autor: ")
                    isbn = input("ISBN (13 dígitos): ")
                    anio = int(input("Año de publicación: "))
                    genero = input("Género literario: ")
                    
                    if tipo == "F":
                        ub = input("Ubicación en estante: ")
                        ej = int(input("Número de ejemplares: "))
                        catalogo.agregar_libro(LibroFisico(titulo, autor, isbn, anio, genero, ub, ej))
                    elif tipo == "D":
                        fmt = input("Formato (PDF/EPUB/MOBI): ")
                        tam = float(input("Tamaño en MB: "))
                        url = input("URL de descarga: ")
                        catalogo.agregar_libro(LibroDigital(titulo, autor, isbn, anio, genero, fmt, tam, url))
                    else:
                        print("Error: Tipo de libro no reconocido.")
                        continue
                    print("¡Libro agregado exitosamente!")

                case "2":
                    query = input("Ingrese término de búsqueda: ")
                    resultados = catalogo.buscar(query)
                    if not resultados:
                        print("No se encontraron libros con ese término.")
                    for lib in resultados:
                        print(f"-> {lib}")

                case "3":
                    tipo = input("Tipo (A: Alumno / P: Profesor / AD: Admin): ").upper()
                    nom = input("Nombre completo: ")
                    em = input("Correo electrónico: ")
                    if tipo == "A":
                        mat = input("Matrícula escolar: ")
                        catalogo.registrar_usuario(Alumno(nom, em, mat))
                    elif tipo == "P":
                        dep = input("Departamento académico: ")
                        catalogo.registrar_usuario(Profesor(nom, em, dep))
                    elif tipo == "AD":
                        car = input("Cargo administrativo: ")
                        catalogo.registrar_usuario(Administrador(nom, em, car))
                    print("Usuario registrado correctamente.")

                case "4":
                    em = input("Email del usuario: ")
                    isbn = input("ISBN del libro: ")
                    print(catalogo.registrar_prestamo(em, isbn))

                case "5":
                    isbn = input("ISBN del libro a devolver: ")
                    print(catalogo.procesar_devolucion(isbn))

                case "6":
                    print(catalogo.ver_cola())

                case "7":
                    print(catalogo.generar_reporte())

                case "8":
                    seed_data(catalogo)

                case "9":
                    catalogo.guardar_json("datos/biblioteca.json")
                    print("\n¡Datos guardados! Gracias por usar el sistema. Saliendo...")
                    break

                case _:
                    print("Opción no válida. Por favor, intente de nuevo.")
        
        except ValueError as ve:
            print(f"\n[ERROR DE DATOS] {ve}")
        except KeyError as ke:
            print(f"\n[ERROR] El dato {ke} no existe en el sistema.")
        except Exception as e:
            print(f"\n[ERROR INESPERADO] {e}")

if __name__ == "__main__":
    main()
