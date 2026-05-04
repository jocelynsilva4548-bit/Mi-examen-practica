from collections import deque
from typing import Tuple, List, Optional
from modelos.usuario import Usuario
from modelos.libro import Libro

class GestorCola:
    """
    Gestiona una cola de espera (FIFO) para libros que no están disponibles.
    Utiliza collections.deque para una gestión eficiente de los extremos.
    """

    def __init__(self) -> None:
        """Inicializa una cola de espera vacía."""
        self._cola: deque = deque()

    def encolar_solicitud(self, usuario: Usuario, libro: Libro) -> None:
        """
        Agrega una nueva solicitud de libro al final de la cola.
        
        Args:
            usuario: El objeto Usuario que solicita el libro.
            libro: El objeto Libro solicitado.
        """
        self._cola.append((usuario, libro))

    def atender_siguiente(self) -> Optional[Tuple[Usuario, Libro]]:
        """
        Atiende y elimina la solicitud más antigua de la cola (el primero en entrar).
        
        Returns:
            Una tupla (Usuario, Libro) o None si la cola está vacía.
        """
        if not self._cola:
            return None
        return self._cola.popleft()

    def ver_cola(self) -> List[Tuple[Usuario, Libro]]:
        """
        Devuelve el estado actual de la cola como una lista.
        
        Returns:
            Una lista con todas las tuplas (Usuario, Libro) en espera.
        """
        return list(self._cola)
