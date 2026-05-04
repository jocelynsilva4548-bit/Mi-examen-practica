import tkinter.messagebox
from modelos.usuario import Alumno, Profesor
from modelos.libro import LibroFisico, LibroDigital
from servicios.catalogo import Catalogo

def probar_sistema():
    print("=== INTEGRACIÓN DEL SISTEMA COMPLETO ===\n")
    
    # Silenciamos alertas de Tkinter
    tkinter.messagebox.showerror = lambda title, message: None

    # 1. Instanciar Catálogo
    cat = Catalogo()

    # 2. Crear y Registrar Libros
    l1 = LibroFisico("Don Quijote", "Cervantes", "9788437604947", 1605, "Clásico", "A1", 2)
    l2 = LibroDigital("Python Master", "Guido", "9781111111111", 2022, "Tech", "PDF", 10.2, "http...")
    cat.agregar_libro(l1)
    cat.agregar_libro(l2)

    # 3. Crear y Registrar Usuarios
    u1 = Alumno("Jocelyn", "jo@correo.com", "MAT-123")
    u2 = Profesor("Dr. House", "house@hospital.com", "Diagnóstico")
    cat.registrar_usuario(u1)
    cat.registrar_usuario(u2)

    print("--- Prueba A: Préstamos ---")
    # Préstamo exitoso
    print(cat.registrar_prestamo("jo@correo.com", "9788437604947"))
    # Intentar prestar el mismo libro (debe fallar)
    print(cat.registrar_prestamo("house@hospital.com", "9788437604947"))
    
    print("\n--- Prueba B: Búsqueda (Protocolo Buscable) ---")
    resultados = cat.buscar("Python")
    for r in resultados:
        print(f"Encontrado: {r.titulo} por {r.autor}")

    print("\n--- Prueba C: Reporte con Duck Typing ---")
    print(cat.generar_reporte())

    print("\n--- Prueba D: Devolución ---")
    print(cat.procesar_devolucion("9788437604947"))
    # Ahora debería estar disponible de nuevo
    print(f"¿Libro disponible después de devolución? {l1.disponible}")

    print("\n=== PRUEBAS FINALIZADAS ===")

if __name__ == "__main__":
    probar_sistema()
