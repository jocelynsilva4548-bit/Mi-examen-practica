from modelos.entidad import Entidad
from modelos.usuario import Usuario, Alumno, Profesor, Administrador
from modelos.libro import Libro, LibroDigital, LibroFisico


def comprobar_herencia() -> None:
    """
    Función de prueba usando Type Hints que demuestra cómo Python
    valida la cadena de herencia de nuestros objetos.
    """
    print("=== PRUEBAS DE HERENCIA (isinstance / issubclass) ===\n")
    
    # Creamos instancias tipadas explícitamente usando Type Hints
    alumno: Alumno = Alumno("Ana García", "ana@correo.com", "A123")
    profesor: Profesor = Profesor("Luis Gómez", "luis@correo.com", "Matemáticas")
    libro_dig: LibroDigital = LibroDigital(
        "Python 101", "Guido van Rossum", "9781234567890", 
        2020, "Programación", "PDF", 5.5, "http://python.org"
    )
    
    print("--- 1. Pruebas con isinstance() ---")
    print(" (Verifica si una VARIABLE es de un tipo o de cualquiera de sus 'padres')\n")
    
    print(f"¿'alumno' es un Alumno?          -> {isinstance(alumno, Alumno)}")
    print(f"¿'alumno' es un Usuario?         -> {isinstance(alumno, Usuario)}")
    print(f"¿'alumno' es una Entidad?        -> {isinstance(alumno, Entidad)}")
    print(f"¿'alumno' es un Libro?           -> {isinstance(alumno, Libro)}") # Obviamente Falso
    
    print(f"\n¿'libro_dig' es LibroDigital?    -> {isinstance(libro_dig, LibroDigital)}")
    print(f"¿'libro_dig' es un Libro?        -> {isinstance(libro_dig, Libro)}")
    # Recuerda que la clase Libro aún NO hereda de Entidad en nuestro código actual:
    print(f"¿'libro_dig' es una Entidad?     -> {isinstance(libro_dig, Entidad)}")

    print("\n\n--- 2. Pruebas con issubclass() ---")
    print(" (Verifica si una CLASE hereda de otra CLASE, sin necesitar variables)\n")
    
    print(f"¿Alumno hereda de Usuario?       -> {issubclass(Alumno, Usuario)}")
    print(f"¿Profesor hereda de Entidad?     -> {issubclass(Profesor, Entidad)}")
    # Administrador no hereda de Alumno, ambos son "hermanos"
    print(f"¿Administrador hereda de Alumno? -> {issubclass(Administrador, Alumno)}")
    
    print(f"\n¿LibroFisico hereda de Libro?    -> {issubclass(LibroFisico, Libro)}")
    print(f"¿Usuario hereda de Entidad?      -> {issubclass(Usuario, Entidad)}")
    
    print("\n=== FIN DE PRUEBAS ===")


if __name__ == "__main__":
    comprobar_herencia()
