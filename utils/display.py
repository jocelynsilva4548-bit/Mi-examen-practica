from modelos.entidad import Entidad

def mostrar_info(item: Entidad) -> None:
    """
    Recibe cualquier objeto que herede de la clase abstracta Entidad.
    Al garantizarse que es una Entidad, sabemos que obligatoriamente
    tiene programado el método __str__() y un atributo 'id'.
    """
    # Usamos str(item) que internamente invoca el método __str__()
    # Además imprimimos los primeros 8 caracteres de su ID único para verificar que lo tiene
    print(f"[ID: {item.id[:8]}] -> {str(item)}")


def crear_tabla(items: list) -> str:
    """
    Genera un reporte de texto simple a partir de una lista de objetos.
    Utiliza DUCK TYPING: no verifica la herencia de los objetos, 
    solo intenta invocar el método to_dict() en ellos.
    """
    if not items:
        return "No hay elementos para mostrar."

    lineas = ["=" * 60]
    lineas.append(f"{'ID (Corto)':<10} | {'TIPO/CLASE':<15} | {'NOMBRE/TÍTULO'}")
    lineas.append("-" * 60)

    for item in items:
        try:
            # Aquí ocurre el Duck Typing: confiamos ciegamente en que 'item' 
            # sabrá responder a 'to_dict()', sin importar de qué clase sea.
            datos = item.to_dict()
            
            # Extraemos los campos más comunes o valores por defecto
            id_corto = str(datos.get('id', 'N/A'))[:8]
            
            # Los usuarios tienen 'tipo', los libros no lo definieron pero son de su clase
            tipo = datos.get('tipo', item.__class__.__name__)
            
            # Los usuarios tienen 'nombre', los libros tienen 'titulo'
            identificador = datos.get('nombre', datos.get('titulo', 'Sin Identificar'))
            
            lineas.append(f"{id_corto:<10} | {tipo:<15} | {identificador}")
            
        except AttributeError:
            # Si el objeto NO tiene el método to_dict(), fallará por aquí
            nombre_clase = item.__class__.__name__
            lineas.append(f"{'ERROR':<10} | {nombre_clase:<15} | ¡No hace 'cuac'! (Falta to_dict)")

    lineas.append("=" * 60)
    return "\n".join(lineas)

