import uuid
from datetime import datetime
from abc import ABC, abstractmethod


class Entidad(ABC):
    """
    Clase base abstracta para todas las entidades del sistema (Libro, Usuario, etc).
    No se pueden crear instancias de esta clase directamente.
    """
    
    def __init__(self):
        # Genera un identificador único universal (UUID) en formato de texto
        self._id = str(uuid.uuid4())
        # Registra la fecha y hora exacta en la que se crea el objeto
        self._fecha_creacion = datetime.now()

    @property
    def id(self) -> str:
        return self._id

    @property
    def fecha_creacion(self) -> datetime:
        return self._fecha_creacion

    @abstractmethod
    def __str__(self) -> str:
        """
        Las clases que hereden de Entidad están OBLIGADAS a implementar 
        su propia versión de este método para representarse como texto.
        """
        pass

    @abstractmethod
    def to_dict(self) -> dict:
        """
        Las clases que hereden de Entidad están OBLIGADAS a implementar 
        cómo convertirse a diccionario (para guardar en base de datos/JSON).
        """
        pass
