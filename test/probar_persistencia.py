import os
import tkinter.messagebox
from modelos.usuario import Alumno
from modelos.libro import LibroFisico
from servicios.catalogo import Catalogo

def probar_persistencia():
    print("=== PRUEBA DE PERSISTENCIA JSON Y BUSCADOR ===\n")
    
    # Silenciar alertas
    tkinter.messagebox.showerror = lambda title, message: None
    
    archivo_test = "test_biblioteca.json"
    cat = Catalogo()

    # 1. Creamos datos iniciales
    print("Creando datos de prueba...")
    u = Alumno("Test User", "test@test.com", "ID-001")
    l = LibroFisico("Libro de Prueba", "Autor Test", "9781111111111", 2023, "Test", "E1", 1)
    cat.registrar_usuario(u)
    cat.agregar_libro(l)
    
    # 2. Guardamos
    print(f"Guardando datos en {archivo_test}...")
    cat.guardar_json(archivo_test)
    
    # 3. Creamos un catálogo nuevo y cargamos
    print("\nCreando segundo catálogo (vacio) y cargando datos...")
    cat2 = Catalogo()
    cat2.cargar_json(archivo_test)
    
    # 4. Probamos el buscador con comprensión de lista
    print("\nProbando buscador en el catálogo cargado:")
    # Buscamos por ISBN (una de las nuevas funciones)
    resultados = cat2.buscar("9781111111111")
    if resultados:
        print(f"Éxito: Se encontró '{resultados[0].titulo}' mediante su ISBN.")
    else:
        print("Fallo: No se encontró el libro por ISBN.")
        
    # Buscamos por título parcial
    resultados_titulo = cat2.buscar("Prueba")
    print(f"Coincidencias por título: {len(resultados_titulo)}")

    # 5. Limpieza
    if os.path.exists(archivo_test):
        os.remove(archivo_test)
        print(f"\nArchivo {archivo_test} eliminado tras la prueba.")

    print("\n=== PRUEBAS FINALIZADAS ===")

if __name__ == "__main__":
    probar_persistencia()
