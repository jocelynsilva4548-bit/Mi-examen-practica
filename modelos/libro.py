from utils.validaciones import validar_isbn13
from modelos.entidad import Entidad

class Libro(Entidad):
    def __init__(self, titulo: str, autor: str, isbn: str, anio: int, genero: str, disponible: bool = True):
        """
        Inicializa un objeto Libro. 
        Al heredar de Entidad, super().__init__() nos genera un ID y fecha_creacion.
        Al asignar a través de 'self.propiedad', forzamos a que pase por los setters y sus validaciones.
        """
        super().__init__()
        self.titulo = titulo
        self.autor = autor
        self.isbn = isbn
        self.anio = anio
        self.genero = genero
        self.disponible = disponible

    # --- TITULO ---
    @property
    def titulo(self) -> str:
        return self._titulo

    @titulo.setter
    def titulo(self, valor: str):
        self._titulo = valor

    # --- AUTOR ---
    @property
    def autor(self) -> str:
        return self._autor

    @autor.setter
    def autor(self, valor: str):
        self._autor = valor

    # --- ISBN ---
    @property
    def isbn(self) -> str:
        return self._isbn

    @isbn.setter
    def isbn(self, valor: str):
        # Llamamos a nuestra función de utilidades para validar
        if validar_isbn13(valor):
            self._isbn = valor
        else:
            raise ValueError("El ISBN proporcionado no es válido.")

    # --- AÑO ---
    @property
    def anio(self) -> int:
        return self._anio

    @anio.setter
    def anio(self, valor: int):
        # Validación de que el año esté en el rango histórico de los libros impresos (aprox) hasta hoy
        if 1440 <= valor <= 2026:
            self._anio = valor
        else:
            raise ValueError("El año de publicación debe estar entre 1440 y 2026.")

    # --- GENERO ---
    @property
    def genero(self) -> str:
        return self._genero

    @genero.setter
    def genero(self, valor: str):
        self._genero = valor

    # --- DISPONIBLE ---
    @property
    def disponible(self) -> bool:
        return self._disponible

    @disponible.setter
    def disponible(self, valor: bool):
        self._disponible = valor

    def __str__(self) -> str:
        estado = "Disponible" if self.disponible else "Prestado/No disponible"
        return f"'{self.titulo}' por {self.autor} ({self.anio}) - ISBN: {self.isbn} [{estado}]"

    def __repr__(self) -> str:
        return (f"Libro(titulo='{self.titulo}', autor='{self.autor}', "
                f"isbn='{self.isbn}', anio={self.anio}, "
                f"genero='{self.genero}', disponible={self.disponible})")

    def __eq__(self, otro) -> bool:
        # Dos libros son el mismo si son objetos Libro y comparten el mismo ISBN
        if not isinstance(otro, Libro):
            return False
        return self.isbn == otro.isbn

    def to_dict(self) -> dict:
        # Convierte el objeto a un diccionario (ideal para guardar en JSON o Base de Datos)
        return {
            "id": self.id,
            "tipo": self.__class__.__name__,
            "titulo": self.titulo,
            "autor": self.autor,
            "isbn": self.isbn,
            "anio": self.anio,
            "genero": self.genero,
            "disponible": self.disponible
        }

    @classmethod
    def from_dict(cls, data: dict):
        # Permite crear un objeto Libro recibiendo un diccionario
        return cls(
            titulo=data.get("titulo", "Sin Título"),
            autor=data.get("autor", "Desconocido"),
            isbn=data.get("isbn", "0000000000000"),
            anio=data.get("anio", 2000),
            genero=data.get("genero", "Desconocido"),
            disponible=data.get("disponible", True)
        )


class LibroDigital(Libro):
    """Subclase que representa un libro en formato digital."""
    def __init__(self, titulo: str, autor: str, isbn: str, anio: int, genero: str, 
                 formato: str, tamano_mb: float, url_descarga: str, disponible: bool = True):
        # Llama al inicializador de la clase padre (Libro)
        super().__init__(titulo, autor, isbn, anio, genero, disponible)
        
        # Atributos propios de LibroDigital
        self.formato = formato
        self.tamano_mb = tamano_mb
        self.url_descarga = url_descarga

    @property
    def formato(self) -> str:
        return self._formato

    @formato.setter
    def formato(self, valor: str):
        formatos_permitidos = ["PDF", "EPUB", "MOBI"]
        # Limpiamos el texto por si tiene un punto (ej: ".pdf") y lo pasamos a mayúsculas
        valor_limpio = valor.upper().replace(".", "")
        if valor_limpio in formatos_permitidos:
            self._formato = valor_limpio
        else:
            raise ValueError(f"El formato debe ser uno de los siguientes: {formatos_permitidos}")

    @property
    def tamano_mb(self) -> float:
        return self._tamano_mb

    @tamano_mb.setter
    def tamano_mb(self, valor: float):
        if valor > 0:
            self._tamano_mb = float(valor)
        else:
            raise ValueError("El tamaño en MB debe ser mayor a 0.")

    @property
    def url_descarga(self) -> str:
        return self._url_descarga

    @url_descarga.setter
    def url_descarga(self, valor: str):
        self._url_descarga = valor

    def to_dict(self) -> dict:
        data = super().to_dict()
        data.update({
            "formato": self.formato,
            "tamano_mb": self.tamano_mb,
            "url_descarga": self.url_descarga
        })
        return data

    @classmethod
    def from_dict(cls, data: dict):
        return cls(
            titulo=data.get("titulo", "Sin Título"),
            autor=data.get("autor", "Desconocido"),
            isbn=data.get("isbn", "0000000000000"),
            anio=data.get("anio", 2000),
            genero=data.get("genero", "Desconocido"),
            formato=data.get("formato", "PDF"),
            tamano_mb=data.get("tamano_mb", 1.0),
            url_descarga=data.get("url_descarga", ""),
            disponible=data.get("disponible", True)
        )

    def __str__(self) -> str:
        # Sobrescribe __str__ agregando etiquetas específicas y reusando el __str__ del padre
        texto_padre = super().__str__()
        return f"[Digital | {self.formato} | {self.tamano_mb}MB] {texto_padre} -> Link: {self.url_descarga}"


class LibroFisico(Libro):
    """Subclase que representa un libro físico en la biblioteca."""
    def __init__(self, titulo: str, autor: str, isbn: str, anio: int, genero: str, 
                 ubicacion: str, num_ejemplares: int, disponible: bool = True):
        # Llama al inicializador de la clase padre (Libro)
        super().__init__(titulo, autor, isbn, anio, genero, disponible)
        
        # Atributos propios de LibroFisico
        self.ubicacion = ubicacion
        self.num_ejemplares = num_ejemplares

    @property
    def ubicacion(self) -> str:
        return self._ubicacion

    @ubicacion.setter
    def ubicacion(self, valor: str):
        self._ubicacion = valor

    @property
    def num_ejemplares(self) -> int:
        return self._num_ejemplares

    @num_ejemplares.setter
    def num_ejemplares(self, valor: int):
        if valor >= 1:
            self._num_ejemplares = int(valor)
        else:
            raise ValueError("Debe haber al menos 1 ejemplar para registrar un libro físico.")

    def to_dict(self) -> dict:
        data = super().to_dict()
        data.update({
            "ubicacion": self.ubicacion,
            "num_ejemplares": self.num_ejemplares
        })
        return data

    @classmethod
    def from_dict(cls, data: dict):
        return cls(
            titulo=data.get("titulo", "Sin Título"),
            autor=data.get("autor", "Desconocido"),
            isbn=data.get("isbn", "0000000000000"),
            anio=data.get("anio", 2000),
            genero=data.get("genero", "Desconocido"),
            ubicacion=data.get("ubicacion", "Desconocida"),
            num_ejemplares=data.get("num_ejemplares", 1),
            disponible=data.get("disponible", True)
        )

    def __str__(self) -> str:
        # Sobrescribe __str__ agregando etiquetas específicas y reusando el __str__ del padre
        texto_padre = super().__str__()
        return f"[Físico | Estante: {self.ubicacion} | Ejemplares: {self.num_ejemplares}] {texto_padre}"
