from utils.formateadores import normalizar_titulo, generar_slug
from utils.reportes import formatear_reporte_libro
from utils.busquedas import buscar_en_texto


def probar_utilidades():
    """Ejecuta pruebas manuales para todas las funciones de utilidades."""
    print("=== INICIANDO PRUEBAS DE UTILIDADES ===\n")

    # ---------------------------------------------------------
    print("--- 1. Pruebas de normalizar_titulo (formateadores.py) ---")
    # Ejemplo 1: Muchos espacios en todos lados
    titulo1 = "   el   principito  "
    print(f"Original : '{titulo1}'\nResultado: '{normalizar_titulo(titulo1)}'\n")

    # Ejemplo 2: Diferentes mayúsculas y minúsculas mezcladas
    titulo2 = "cien   AÑOS de soledad"
    print(f"Original : '{titulo2}'\nResultado: '{normalizar_titulo(titulo2)}'\n")

    # ---------------------------------------------------------
    print("--- 2. Pruebas de generar_slug (formateadores.py) ---")
    # Ejemplo 1: Con ñ, signos de exclamación y mayúsculas
    texto1 = "¡Cien Años de Soledad!"
    print(f"Original : '{texto1}'\nSlug     : '{generar_slug(texto1)}'\n")

    # Ejemplo 2: Con acentos convencionales
    texto2 = "Crónica de una Muerte Anunciada"
    print(f"Original : '{texto2}'\nSlug     : '{generar_slug(texto2)}'\n")

    # ---------------------------------------------------------
    print("--- 3. Pruebas de formatear_reporte_libro (reportes.py) ---")
    # Ejemplo 1: Diccionario básico de libro
    libro1 = {
        "titulo": "El Hobbit", 
        "autor": "J.R.R. Tolkien", 
        "año": 1937, 
        "estado": "Disponible"
    }
    print("Reporte 1:")
    print(formatear_reporte_libro(libro1))

    # Ejemplo 2: Diferentes claves para ver cómo se alinean
    libro2 = {
        "titulo": "1984", 
        "genero": "Distopía", 
        "paginas": 328, 
        "isbn": "978-0451524935"
    }
    print("\nReporte 2:")
    print(formatear_reporte_libro(libro2) + "\n")

    # ---------------------------------------------------------
    print("--- 4. Pruebas de buscar_en_texto (busquedas.py) ---")
    texto_largo = "En un lugar de la Mancha, de cuyo nombre no quiero acordarme"
    print(f"Texto base: '{texto_largo}'\n")

    # Ejemplo 1: Coincidencia exitosa (ignora que buscamos en mayúsculas)
    busqueda1 = "MANCHA"
    resultado1 = buscar_en_texto(texto_largo, busqueda1)
    print(f"¿Contiene '{busqueda1}'?: {resultado1}")

    # Ejemplo 2: Búsqueda fallida
    busqueda2 = "Quijote"
    resultado2 = buscar_en_texto(texto_largo, busqueda2)
    print(f"¿Contiene '{busqueda2}'?: {resultado2}\n")

    print("=== PRUEBAS FINALIZADAS ===")


if __name__ == "__main__":
    probar_utilidades()
