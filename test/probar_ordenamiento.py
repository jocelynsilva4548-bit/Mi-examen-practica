import tkinter.messagebox
from modelos.libro import LibroFisico

def probar_ordenamiento():
    print("=== PRUEBA DE ORDENAMIENTO CON LAMBDA ===\n")
    
    # Silenciamos alertas visuales
    tkinter.messagebox.showerror = lambda title, message: None

    # Creamos una lista de libros desordenada
    biblioteca = [
        LibroFisico("Don Quijote", "Cervantes", "9788437604947", 1605, "Clásico", "A1", 1),
        LibroFisico("Cien Años de Soledad", "García Márquez", "9780060883287", 1967, "Realismo", "B2", 1),
        LibroFisico("1984", "George Orwell", "9780451524935", 1949, "Distopía", "C3", 1),
        LibroFisico("Zulú", "Autor Desconocido", "9781234567890", 2010, "Aventura", "D4", 1)
    ]

    print("Lista original:")
    for libro in biblioteca:
        print(f" - {libro.titulo}")

    # ORDENAMIENTO CON LAMBDA
    # La función sorted toma una lista y una 'key' que define bajo qué criterio ordenar.
    # lambda x: x.titulo le dice a Python: "De cada objeto x, usa su atributo titulo para comparar".
    libros_ordenados = sorted(biblioteca, key=lambda x: x.titulo)

    print("\nLista ordenada por título (Ascendente):")
    for libro in libros_ordenados:
        print(f" - {libro.titulo}")

    print("\n=== PRUEBAS FINALIZADAS ===")

if __name__ == "__main__":
    probar_ordenamiento()
