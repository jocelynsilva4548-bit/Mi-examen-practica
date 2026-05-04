from modelos.libro import Libro
import tkinter.messagebox

def probar_clase_libro():
    print("=== INICIANDO PRUEBAS DE CLASE LIBRO ===\n")
    
    # Simulador para la alerta de Tkinter
    tkinter.messagebox.showerror = lambda title, message: print(f"\n>> [ALERTA VISUAL SIMULADA] {title}: {message}")

    try:
        print("--- 1. Creando 3 ejemplos de libros válidos ---")
        libro1 = Libro(
            titulo="Cien Años de Soledad",
            autor="Gabriel García Márquez",
            isbn="9780060883287",
            anio=1967,
            genero="Realismo Mágico"
        )
        
        libro2 = Libro(
            titulo="1984",
            autor="George Orwell",
            isbn="9780451524935",
            anio=1949,
            genero="Distopía",
            disponible=False
        )

        libro3 = Libro(
            titulo="Don Quijote de la Mancha",
            autor="Miguel de Cervantes",
            isbn="9788437604947",
            anio=1605,
            genero="Novela Clásica"
        )

        print(f"Libro 1 (__str__): {libro1}")
        print(f"Libro 2 (__str__): {libro2}")
        print(f"Libro 3 (__str__): {libro3}")

        print("\n--- 2. Probando __repr__ en uno de ellos ---")
        print(f"Representación técnica: {repr(libro2)}")
        
        print("\n--- 3. Probando to_dict() y from_dict() con el Libro 3 ---")
        dic_libro3 = libro3.to_dict()
        print(f"Diccionario exportado: {dic_libro3}")
        
        libro3_clon = Libro.from_dict(dic_libro3)
        print(f"Libro reconstruido: {libro3_clon}")
        
        print("\n--- 4. Probando igualdad (__eq__) ---")
        print(f"¿Libro 3 es igual a su clon? {libro3 == libro3_clon}")
        print(f"¿Libro 1 es igual al Libro 2? {libro1 == libro2}")
        
        print("\n--- 5. Probando validaciones restrictivas (Errores esperados) ---")
        try:
            libro_invalido_isbn = Libro("Error", "Autor", "123", 2000, "Test")
            print("ERROR: ¡Se creó un libro con ISBN malo!")
        except ValueError as e:
            print(f"Validación ISBN exitosa. El sistema lo bloqueó con: {e}")

        try:
            libro_invalido_anio = Libro("Antiguo", "Autor", "9781234567890", 1200, "Test")
            print("ERROR: ¡Se creó un libro demasiado antiguo!")
        except ValueError as e:
            print(f"Validación Año exitosa. El sistema lo bloqueó con: {e}")
            
    except Exception as e:
        print(f"Hubo un error inesperado durante las pruebas: {e}")

    print("\n=== PRUEBAS FINALIZADAS ===")

if __name__ == "__main__":
    probar_clase_libro()
