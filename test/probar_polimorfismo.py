import tkinter.messagebox
from modelos.usuario import Alumno, Profesor, Administrador
from modelos.libro import LibroDigital, LibroFisico
from utils.display import mostrar_info

def probar_polimorfismo():
    print("=== INICIANDO PRUEBA DE POLIMORFISMO ===\n")
    
    # Silenciamos la alerta de validación visual de Tkinter para la prueba
    tkinter.messagebox.showerror = lambda title, message: None

    # Creamos una lista mezclada con todo tipo de objetos que hemos programado
    lista_mixta = [
        Alumno("Carlos", "carlos@correo.com", "A-999"),
        LibroDigital("Aprende Python", "Guido", "9781234567890", 2021, "Educación", "PDF", 12.5, "http..."),
        Administrador("Jefa de Biblioteca", "admin@correo.com", "Directora"),
        Profesor("Dr. López", "lopez@correo.com", "Ciencias"),
        LibroFisico("Cálculo 1", "Stewart", "9780534393212", 2005, "Matemáticas", "Estante B-1", 5)
    ]

    print("Pasando la lista mixta por la función 'mostrar_info':\n")
    
    # La magia del polimorfismo: el ciclo for no sabe qué tipo de objeto es exactamente,
    # solo sabe que se lo pasa a mostrar_info() y esta función hace su trabajo.
    for objeto in lista_mixta:
        mostrar_info(objeto)

    print("\n=== PRUEBAS FINALIZADAS ===")

if __name__ == "__main__":
    probar_polimorfismo()
