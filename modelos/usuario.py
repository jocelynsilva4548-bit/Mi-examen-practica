from abc import abstractmethod
from modelos.entidad import Entidad
from utils.constantes import MAXIMO_LIBROS_ALUMNOS, MAXIMO_LIBROS_PROFESORES


class Usuario(Entidad):
    """
    Clase base abstracta para los usuarios del sistema.
    Hereda de Entidad, obteniendo un ID y una fecha de creación automáticos.
    """

    def __init__(self, nombre: str, correo: str):
        super().__init__()
        self.nombre = nombre
        self.correo = correo
        # Todos los usuarios pueden tener libros prestados
        self.libros_prestados = []

    @abstractmethod
    def puede_pedir_prestado(self) -> bool:
        """
        Obliga a las clases hijas a definir si pueden o no llevarse otro libro.
        """
        pass


class Alumno(Usuario):
    """Representa a un estudiante en la biblioteca."""
    
    def __init__(self, nombre: str, correo: str, matricula: str):
        super().__init__(nombre, correo)
        self.matricula = matricula

    def puede_pedir_prestado(self) -> bool:
        # Verifica contra la constante si ya alcanzó su límite
        return len(self.libros_prestados) < MAXIMO_LIBROS_ALUMNOS

    def to_dict(self) -> dict:
        return {
            "id": self.id,
            "tipo": "Alumno",
            "nombre": self.nombre,
            "correo": self.correo,
            "matricula": self.matricula,
            "libros_prestados": [libro.isbn for libro in self.libros_prestados]
        }

    @classmethod
    def from_dict(cls, data: dict):
        return cls(
            nombre=data.get("nombre", "Sin Nombre"),
            correo=data.get("correo", "Sin Correo"),
            matricula=data.get("matricula", "N/A")
        )

    def __str__(self) -> str:
        return f"[Alumno] {self.nombre} ({self.matricula}) | Libros: {len(self.libros_prestados)}/{MAXIMO_LIBROS_ALUMNOS}"


class Profesor(Usuario):
    """Representa a un profesor en la biblioteca, con límites extendidos."""
    
    def __init__(self, nombre: str, correo: str, departamento: str):
        super().__init__(nombre, correo)
        self.departamento = departamento

    def puede_pedir_prestado(self) -> bool:
        # Verifica contra la constante de profesores
        return len(self.libros_prestados) < MAXIMO_LIBROS_PROFESORES

    def to_dict(self) -> dict:
        return {
            "id": self.id,
            "tipo": "Profesor",
            "nombre": self.nombre,
            "correo": self.correo,
            "departamento": self.departamento,
            "libros_prestados": [libro.isbn for libro in self.libros_prestados]
        }

    @classmethod
    def from_dict(cls, data: dict):
        return cls(
            nombre=data.get("nombre", "Sin Nombre"),
            correo=data.get("correo", "Sin Correo"),
            departamento=data.get("departamento", "N/A")
        )

    def __str__(self) -> str:
        return f"[Profesor] {self.nombre} (Depto: {self.departamento}) | Libros: {len(self.libros_prestados)}/{MAXIMO_LIBROS_PROFESORES}"


class Administrador(Usuario):
    """Representa al personal de la biblioteca. Tiene acceso ilimitado."""
    
    def __init__(self, nombre: str, correo: str, cargo: str = "Bibliotecario"):
        super().__init__(nombre, correo)
        self.cargo = cargo

    def puede_pedir_prestado(self) -> bool:
        # El administrador/bibliotecario no tiene límite de préstamos en el sistema
        return True

    def to_dict(self) -> dict:
        return {
            "id": self.id,
            "tipo": "Administrador",
            "nombre": self.nombre,
            "correo": self.correo,
            "cargo": self.cargo,
            "libros_prestados": [libro.isbn for libro in self.libros_prestados]
        }

    @classmethod
    def from_dict(cls, data: dict):
        return cls(
            nombre=data.get("nombre", "Sin Nombre"),
            correo=data.get("correo", "Sin Correo"),
            cargo=data.get("cargo", "Bibliotecario")
        )

    def __str__(self) -> str:
        return f"[Admin] {self.nombre} - Cargo: {self.cargo}"
