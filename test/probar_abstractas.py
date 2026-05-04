from modelos.entidad import Entidad
from modelos.usuario import Usuario

def probar_proteccion_abstracta():
    """
    Intenta crear objetos de clases abstractas para demostrar
    cómo Python bloquea estas acciones mediante un TypeError.
    """
    print("=== INICIANDO PRUEBAS DE PROTECCIÓN ABSTRACTA ===\n")

    # Prueba 1: Clase Entidad
    print("--- Prueba 1: Intentando crear un objeto 'Entidad' puro ---")
    try:
        # Esto debería fallar porque tiene métodos abstractos (to_dict y __str__)
        entidad_fantasma = Entidad()
        print("FALLO: Se logró crear una Entidad. ¡La protección no funcionó!")
    except TypeError as error_capturado:
        print(f"EXITO! Python protegió el sistema bloqueando la creación.")
        print(f"   Mensaje de Python: {error_capturado}\n")

    # Prueba 2: Clase Usuario
    print("--- Prueba 2: Intentando crear un objeto 'Usuario' genérico ---")
    try:
        # Esto debería fallar porque hereda los abstractos de Entidad 
        # y además suma su propio método abstracto (puede_pedir_prestado)
        usuario_fantasma = Usuario(nombre="Juan Pérez", correo="juan@biblioteca.com")
        print("FALLO: Se logró crear un Usuario genérico. ¡La protección no funcionó!")
    except TypeError as error_capturado:
        print(f"EXITO! Python protegió el sistema bloqueando la creación.")
        print(f"   Mensaje de Python: {error_capturado}\n")

    print("=== PRUEBAS FINALIZADAS ===")

if __name__ == "__main__":
    probar_proteccion_abstracta()
