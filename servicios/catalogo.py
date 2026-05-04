import json
from typing import Protocol, List, Dict, Optional
from datetime import datetime
from modelos.libro import Libro, LibroDigital, LibroFisico
from modelos.usuario import Usuario, Alumno, Profesor, Administrador
from servicios.gestor_cola import GestorCola
from servicios.historial import Historial
from utils.display import crear_tabla


class Buscable(Protocol):
    def buscar(self, query: str) -> list:
        ...


class Catalogo:
    def __init__(self) -> None:
        """Inicializa el catálogo con colecciones vacías y servicios integrados."""
        self.libros: List[Libro] = []
        self.usuarios: Dict[str, Usuario] = {}
        self.prestamos: List[dict] = []
        # Integración de nuevos servicios
        self.cola_espera = GestorCola()
        self.historial = Historial()

    def agregar_libro(self, libro: Libro) -> None:
        self.libros.append(libro)
        self.historial.registrar_accion(f"Agregado libro: {libro.titulo}")

    def eliminar_libro(self, isbn: str) -> bool:
        for i, libro in enumerate(self.libros):
            if libro.isbn == isbn:
                self.libros.pop(i)
                self.historial.registrar_accion(f"Eliminado libro ISBN: {isbn}")
                return True
        return False

    def registrar_usuario(self, usuario: Usuario) -> None:
        self.usuarios[usuario.correo] = usuario
        self.historial.registrar_accion(f"Registrado usuario: {usuario.nombre}")

    def registrar_prestamo(self, email_usuario: str, isbn_libro: str) -> str:
        usuario = self.usuarios.get(email_usuario)
        libro = next((l for l in self.libros if l.isbn == isbn_libro), None)

        if not usuario: return "Error: Usuario no encontrado."
        if not libro: return "Error: Libro no encontrado."
        if not libro.disponible: 
            # Si no está disponible, lo encolamos automáticamente
            self.cola_espera.encolar_solicitud(usuario, libro)
            return f"Info: '{libro.titulo}' no disponible. {usuario.nombre} agregado a cola de espera."
        
        if not usuario.puede_pedir_prestado():
            return f"Error: {usuario.nombre} alcanzó su límite."

        libro.disponible = False
        usuario.libros_prestados.append(libro)
        
        registro = {
            "usuario": usuario.nombre,
            "email": usuario.correo,
            "libro": libro.titulo,
            "isbn": libro.isbn,
            "fecha": datetime.now().strftime("%Y-%m-%d %H:%M")
        }
        self.prestamos.append(registro)
        self.historial.registrar_accion(f"Préstamo: {libro.titulo} -> {usuario.nombre}")
        return f"Éxito: Préstamo registrado."

    def procesar_devolucion(self, isbn_libro: str) -> str:
        libro = next((l for l in self.libros if l.isbn == isbn_libro), None)
        if not libro or libro.disponible: return "Error: El libro ya está en biblioteca."

        usuario_con_libro = next((u for u in self.usuarios.values() if libro in u.libros_prestados), None)
        
        if usuario_con_libro:
            usuario_con_libro.libros_prestados.remove(libro)
            libro.disponible = True
            self.prestamos = [p for p in self.prestamos if p['isbn'] != isbn_libro]
            self.historial.registrar_accion(f"Devolución: {libro.titulo} de {usuario_con_libro.nombre}")
            return f"Éxito: Devolución procesada."
        return "Error: No se encontró registro del préstamo."

    def buscar(self, query: str) -> list:
        q = query.lower()
        return [l for l in self.libros if q in l.titulo.lower() or q in l.autor.lower() or q in l.isbn]

    def ver_cola(self) -> str:
        cola = self.cola_espera.ver_cola()
        if not cola: return "La cola de espera está vacía."
        res = "--- COLA DE ESPERA ---\n"
        for i, (u, l) in enumerate(cola, 1):
            res += f"{i}. {u.nombre} esperando por '{l.titulo}'\n"
        return res

    def guardar_json(self, nombre_archivo: str = "datos/biblioteca.json") -> None:
        import os
        os.makedirs(os.path.dirname(nombre_archivo), exist_ok=True)
        data = {
            "libros": [l.to_dict() for l in self.libros],
            "usuarios": [u.to_dict() for u in self.usuarios.values()],
            "prestamos": self.prestamos
        }
        with open(nombre_archivo, 'w', encoding='utf-8') as f:
            json.dump(data, f, indent=4, ensure_ascii=False)
        print(f"Datos guardados exitosamente en {nombre_archivo}")

    def cargar_json(self, nombre_archivo: str = "datos/biblioteca.json") -> None:
        """
        Carga el estado del catálogo desde un archivo JSON.
        Maneja errores de archivo no encontrado de forma silenciosa.
        """
        try:
            with open(nombre_archivo, 'r', encoding='utf-8') as f:
                data = json.load(f)
        except (FileNotFoundError, json.JSONDecodeError):
            print(f"Aviso: No se pudo cargar {nombre_archivo}. Iniciando vacío.")
            return
        
        self.libros = []
        for item in data.get("libros", []):
            tipo = item.get("tipo")
            if tipo == "LibroDigital": obj = LibroDigital.from_dict(item)
            elif tipo == "LibroFisico": obj = LibroFisico.from_dict(item)
            else: obj = Libro.from_dict(item)
            obj._id = item.get("id", obj.id)
            self.libros.append(obj)
        
        self.usuarios = {}
        for item in data.get("usuarios", []):
            tipo = item.get("tipo")
            if tipo == "Alumno": obj = Alumno.from_dict(item)
            elif tipo == "Profesor": obj = Profesor.from_dict(item)
            elif tipo == "Administrador": obj = Administrador.from_dict(item)
            else: continue
            obj._id = item.get("id", obj.id)
            isbns = item.get("libros_prestados", [])
            for isbn in isbns:
                libro = next((l for l in self.libros if l.isbn == isbn), None)
                if libro: 
                    obj.libros_prestados.append(libro)
                    libro.disponible = False
            self.usuarios[obj.correo] = obj
        
        self.prestamos = data.get("prestamos", [])
        print(f"Datos cargados desde {nombre_archivo}")

    def generar_reporte(self) -> str:
        return crear_tabla(self.libros)
