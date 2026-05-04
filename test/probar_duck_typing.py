import tkinter.messagebox
from modelos.usuario import Alumno, Administrador
from modelos.libro import LibroDigital
from utils.display import crear_tabla

class PatoDeGomaInfiltrado:
    """
    Esta es una clase de "juguete" que NO hereda de Entidad, NO es un Usuario, 
    ni tampoco es un Libro. Sin embargo, tiene un método llamado to_dict().
    """
    def to_dict(self):
        return {
            "id": "11111111",
            "tipo": "Juguete Baño",
            "nombre": "Sr. Cuackers"
        }

class Piedra:
    """
    Esta es otra clase de "juguete", pero esta NO tiene el método to_dict().
    """
    pass

def probar_duck_typing():
    print("=== INICIANDO PRUEBA DE DUCK TYPING ===\n")
    
    # Silenciamos la alerta de validación visual de Tkinter para la prueba
    tkinter.messagebox.showerror = lambda title, message: None

    lista_mixta = [
        Alumno("Carlos", "carlos@correo.com", "A-999"),
        LibroDigital("Aprende Python", "Guido", "9781234567890", 2021, "Educación", "PDF", 12.5, "http..."),
        Administrador("Jefa de Biblioteca", "admin@correo.com", "Directora"),
        PatoDeGomaInfiltrado(),  # ¡Este objeto no tiene nada que ver con el sistema!
        Piedra()                 # ¡Este ni siquiera tiene el método!
    ]

    reporte = crear_tabla(lista_mixta)
    print(reporte)

    print("\n=== PRUEBAS FINALIZADAS ===")

if __name__ == "__main__":
    probar_duck_typing()
