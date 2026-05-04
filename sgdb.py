import tkinter as tk
from tkinter import ttk, messagebox, simpledialog
from servicios.catalogo import Catalogo

class SGDBApp:
    """
    Clase principal de la interfaz gráfica del SGDB.
    Maneja la visualización de datos y la interacción con el usuario.
    """
    def __init__(self, root: tk.Tk) -> None:
        self.root = root
        self.root.title("SGDB - Sistema de Gestión de Biblioteca Digital")
        self.root.geometry("900x600")
        self.root.minsize(700, 500)
        
        # Inicializar el motor del sistema (Catalogo)
        self.catalogo = Catalogo()
        
        # Intentar cargar datos existentes
        try:
            self.catalogo.cargar_json("datos/biblioteca.json")
        except FileNotFoundError:
            pass
        except Exception as e:
            messagebox.showwarning("Aviso", f"No se pudieron cargar los datos previos: {e}")
        
        # Configurar colores y estilos básicos
        self.setup_styles()
        
        # Crear la interfaz
        self.create_widgets()

    def setup_styles(self) -> None:
        """Configura el tema y colores globales de la aplicación."""
        style = ttk.Style()
        style.theme_use('clam')
        self.root.configure(bg="#f4f4f9")

    def create_widgets(self) -> None:
        """Crea y posiciona los componentes visuales de la ventana."""
        self.main_frame = tk.Frame(self.root, bg="#f4f4f9")
        self.main_frame.pack(fill=tk.BOTH, expand=True, padx=20, pady=20)
        
        # Título
        lbl_title = tk.Label(
            self.main_frame, 
            text="Sistema de Gestión de Biblioteca Digital", 
            font=("Segoe UI", 24, "bold"), 
            bg="#f4f9f8", 
            fg="#333333"
        )
        lbl_title.pack(pady=(0, 20))
        
        # Menú de acciones
        menu_frame = tk.Frame(self.main_frame, bg="#f4f4f9")
        menu_frame.pack(fill=tk.X, pady=10)
        
        btn_prestar = ttk.Button(menu_frame, text="Realizar Préstamo", command=self.accion_prestar)
        btn_prestar.pack(side=tk.LEFT, padx=5)
        
        btn_devolver = ttk.Button(menu_frame, text="Procesar Devolución", command=self.accion_devolver)
        btn_devolver.pack(side=tk.LEFT, padx=5)
        
        btn_guardar = ttk.Button(menu_frame, text="Guardar Cambios", command=self.accion_guardar)
        btn_guardar.pack(side=tk.LEFT, padx=5)
        
        btn_salir = ttk.Button(menu_frame, text="Salir", command=self.root.quit)
        btn_salir.pack(side=tk.RIGHT, padx=5)
        
        # Área de tabla (Inventario)
        self.content_frame = tk.Frame(self.main_frame, bg="white", bd=1, relief=tk.SOLID)
        self.content_frame.pack(fill=tk.BOTH, expand=True, pady=10)
        
        columns = ("id", "titulo", "autor", "isbn", "estado")
        self.tree = ttk.Treeview(self.content_frame, columns=columns, show="headings")
        
        self.tree.heading("id", text="ID")
        self.tree.heading("titulo", text="Título")
        self.tree.heading("autor", text="Autor")
        self.tree.heading("isbn", text="ISBN")
        self.tree.heading("estado", text="Estado")
        
        self.tree.column("id", width=50, anchor=tk.CENTER)
        self.tree.column("titulo", width=250)
        self.tree.column("autor", width=150)
        self.tree.column("isbn", width=100)
        self.tree.column("estado", width=100, anchor=tk.CENTER)
        
        scrollbar = ttk.Scrollbar(self.content_frame, orient=tk.VERTICAL, command=self.tree.yview)
        self.tree.configure(yscroll=scrollbar.set)
        
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        self.tree.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        
        self.refresh_table()

    def refresh_table(self) -> None:
        """Limpia y vuelve a llenar la tabla con los datos actuales del catálogo."""
        for item in self.tree.get_children():
            self.tree.delete(item)
            
        for libro in self.catalogo.libros:
            estado = "Disponible" if libro.disponible else "Prestado"
            self.tree.insert("", tk.END, values=(libro.id[:8], libro.titulo, libro.autor, libro.isbn, estado))

    def accion_prestar(self) -> None:
        """Solicita datos y procesa un préstamo."""
        email = simpledialog.askstring("Préstamo", "Ingrese el correo del usuario:")
        if not email: return
        
        isbn = simpledialog.askstring("Préstamo", "Ingrese el ISBN del libro:")
        if not isbn: return
        
        resultado = self.catalogo.registrar_prestamo(email, isbn)
        if "Éxito" in resultado:
            messagebox.showinfo("Éxito", resultado)
            self.refresh_table()
        elif "Info" in resultado:
            messagebox.showinfo("Información", resultado)
        else:
            messagebox.showerror("Error", resultado)

    def accion_devolver(self) -> None:
        """Solicita datos y procesa una devolución."""
        isbn = simpledialog.askstring("Devolución", "Ingrese el ISBN del libro a devolver:")
        if not isbn: return
        
        resultado = self.catalogo.procesar_devolucion(isbn)
        if "Éxito" in resultado:
            messagebox.showinfo("Éxito", resultado)
            self.refresh_table()
        else:
            messagebox.showerror("Error", resultado)

    def accion_guardar(self) -> None:
        """Guarda el estado actual en el archivo JSON."""
        try:
            self.catalogo.guardar_json("datos/biblioteca.json")
            messagebox.showinfo("Guardado", "Los datos se han guardado correctamente.")
        except Exception as e:
            messagebox.showerror("Error", f"No se pudo guardar: {e}")

def main() -> None:
    root = tk.Tk()
    app = SGDBApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()
