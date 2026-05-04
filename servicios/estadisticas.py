from collections import Counter, defaultdict, deque
from typing import List, Dict, Tuple, Any, Set

class GeneradorEstadisticas:
    """
    Clase encargada de procesar grandes volúmenes de datos de la biblioteca
    para extraer información útil mediante estructuras de datos avanzadas.
    """

    def __init__(self, prestamos: List[Dict[str, Any]], catalogo_libros: List[Dict[str, Any]]):
        """
        Inicializa el generador con los datos del sistema.
        
        Args:
            prestamos: Una LISTA de diccionarios con información de préstamos.
            catalogo_libros: Una LISTA de diccionarios con información técnica de los libros.
        """
        self.prestamos = prestamos
        self.catalogo_libros = catalogo_libros
        # Demostración de DEQUE: Mantenemos un registro de las últimas 5 operaciones de estadística
        self.historial_calculos = deque(maxlen=5)

    def obtener_libro_mas_prestado(self) -> Tuple[str, int]:
        """Usa collections.Counter para encontrar el libro más popular."""
        # Comprensión de lista para extraer títulos
        titulos = [p["libro"] for p in self.prestamos]
        conteo = Counter(titulos)
        
        self.historial_calculos.append("Cálculo de libro popular")
        # Retorna una TUPLA (elemento, cuenta)
        return conteo.most_common(1)[0] if conteo else ("Ninguno", 0)

    def obtener_usuario_top(self) -> Tuple[str, int]:
        """Encuentra al usuario con más actividad en el sistema."""
        usuarios = [p["usuario"] for p in self.prestamos]
        conteo = Counter(usuarios)
        
        self.historial_calculos.append("Cálculo de usuario top")
        return conteo.most_common(1)[0] if conteo else ("Ninguno", 0)

    def calcular_multa_promedio(self, lista_multas: List[float]) -> float:
        """Calcula el promedio simple de una lista de valores numéricos."""
        if not lista_multas:
            return 0.0
        promedio = sum(lista_multas) / len(lista_multas)
        self.historial_calculos.append(f"Cálculo de promedio: {promedio}")
        return promedio

    def obtener_distribucion_por_genero(self) -> Dict[str, int]:
        """Usa collections.defaultdict para agrupar libros por su género literario."""
        # Usamos un defaultdict para evitar errores de llave inexistente
        generos_cont = defaultdict(int)
        
        # Usamos un SET para identificar qué títulos únicos han sido prestados alguna vez
        titulos_prestados: Set[str] = {p["libro"] for p in self.prestamos}

        for libro in self.catalogo_libros:
            if libro["titulo"] in titulos_prestados:
                genero = libro.get("genero", "Desconocido")
                generos_cont[genero] += 1
        
        self.historial_calculos.append("Cálculo de géneros")
        # Convertimos a DICT estándar para la salida
        return dict(generos_cont)

    def ver_resumen_estructuras(self) -> str:
        """Demuestra el estado de las diversas estructuras utilizadas."""
        resumen = (
            f"Historial de Cálculos (deque): {list(self.historial_calculos)}\n"
            f"Total de Préstamos procesados (list): {len(self.prestamos)}\n"
            f"Libros únicos en préstamos (set): {len({p['libro'] for p in self.prestamos})}"
        )
        return resumen


# --- EJEMPLO DE USO ---
if __name__ == "__main__":
    # 1. Datos de ejemplo (Listas de Diccionarios)
    libros_ejemplo = [
        {"titulo": "Python 101", "genero": "Tecnología"},
        {"titulo": "Cálculo I", "genero": "Matemáticas"},
        {"titulo": "Don Quijote", "genero": "Literatura"},
        {"titulo": "El Hobbit", "genero": "Fantasía"}
    ]

    prestamos_ejemplo = [
        {"usuario": "Ana", "libro": "Python 101"},
        {"usuario": "Beto", "libro": "Cálculo I"},
        {"usuario": "Ana", "libro": "El Hobbit"},
        {"usuario": "Ana", "libro": "Python 101"},
        {"usuario": "Carlos", "libro": "Cálculo I"}
    ]

    multas_ejemplo = [50.0, 20.5, 100.0, 0.0]

    # 2. Instanciación y Ejecución
    stats = GeneradorEstadisticas(prestamos_ejemplo, libros_ejemplo)

    print("=== REPORTES DE ESTADÍSTICAS ===")
    
    pop, cant = stats.obtener_libro_mas_prestado()
    print(f"Libro más prestado: {pop} ({cant} veces)")

    user, u_cant = stats.obtener_usuario_top()
    print(f"Usuario más activo: {user} ({u_cant} préstamos)")

    print(f"Multa promedio: ${stats.calcular_multa_promedio(multas_ejemplo):.2f}")
    
    print(f"Distribución por Géneros: {stats.obtener_distribucion_por_genero()}")
    
    print("\n--- Demostración de Estructuras Internas ---")
    print(stats.ver_resumen_estructuras())
