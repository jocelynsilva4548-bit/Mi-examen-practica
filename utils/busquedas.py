def buscar_en_texto(haystack: str, needle: str) -> bool:
    """
    Busca una palabra exacta o fragmento de texto (needle) dentro de 
    un texto más largo (haystack). Ignora mayúsculas y minúsculas.
    """
    # Convertimos ambos textos a minúsculas para que la comparación sea justa
    texto_largo_minusculas = haystack.lower()
    palabra_buscar_minusculas = needle.lower()
    
    # El operador 'in' de Python verifica si un texto está dentro de otro
    if palabra_buscar_minusculas in texto_largo_minusculas:
        return True
    else:
        return False
