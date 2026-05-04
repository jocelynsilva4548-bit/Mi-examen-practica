import unicodedata

def normalizar_titulo(titulo: str) -> str:
    """
    Normaliza un título o texto quitando espacios innecesarios y 
    aplicando mayúsculas iniciales.

    Ejemplo:
    >>> normalizar_titulo(' el   quijote ')
    'El Quijote'
    """
    # 1. strip() quita los espacios al inicio y al final
    texto_sin_bordes = titulo.strip()
    
    # 2. split() divide el texto en una lista de palabras ignorando espacios múltiples,
    # y " ".join() las vuelve a unir usando exactamente un solo espacio.
    palabras = texto_sin_bordes.split()
    texto_espaciado_correcto = " ".join(palabras)
    
    # 3. title() convierte la primera letra de cada palabra a mayúscula
    resultado_final = texto_espaciado_correcto.title()
    
    return resultado_final


def generar_slug(texto: str) -> str:
    """
    Convierte un texto a formato URL (slug).
    Quita acentos, convierte a minúsculas y usa guiones en lugar de espacios.
    """
    # 1. Separar las letras de sus acentos
    texto_separado = unicodedata.normalize('NFD', texto)
    
    # 2. Eliminar los acentos forzando el texto a formato ASCII
    texto_sin_acentos = texto_separado.encode('ascii', 'ignore').decode('utf-8')
    
    # 3. Convertir a minúsculas y reemplazar espacios por guiones
    slug = texto_sin_acentos.lower().replace(" ", "-")
    
    return slug

