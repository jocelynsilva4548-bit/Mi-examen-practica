def formatear_reporte_libro(libro_dict: dict) -> str:
    """
    Toma un diccionario con los datos de un libro y devuelve
    un texto con la información formateada en columnas alineadas.
    """
    reporte = "--- DATOS DEL LIBRO ---\n"
    
    for clave, valor in libro_dict.items():
        # .capitalize() pone la primera letra en mayúscula (ej. 'titulo' -> 'Titulo')
        # .ljust(15) rellena con espacios a la derecha hasta llegar a 15 caracteres
        clave_alineada = str(clave).capitalize().ljust(15)
        reporte += f"{clave_alineada}: {valor}\n"
        
    reporte += "-----------------------"
    
    return reporte
