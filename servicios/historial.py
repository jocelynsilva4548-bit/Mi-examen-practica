from typing import List, Optional, Any

class Historial:
    """
    Gestiona un historial de acciones utilizando una estructura de Pila (LIFO).
    Permite registrar acciones y deshacer la última realizada.
    """

    def __init__(self) -> None:
        """Inicializa un historial vacío."""
        self._pila: List[Any] = []

    def registrar_accion(self, accion: str) -> None:
        """
        Agrega una nueva acción al historial (cima de la pila).
        
        Args:
            accion: Una cadena de texto que describe la acción realizada.
        """
        self._pila.append(accion)

    def deshacer_ultima(self) -> Optional[str]:
        """
        Elimina y devuelve la última acción registrada (la más reciente).
        
        Returns:
            La descripción de la acción eliminada o None si el historial está vacío.
        """
        if not self._pila:
            return None
        return self._pila.pop()

    def ver_historial(self) -> List[str]:
        """
        Devuelve una copia del historial de acciones.
        
        Returns:
            Una lista con todas las acciones registradas, desde la más antigua a la más reciente.
        """
        return self._pila.copy()
