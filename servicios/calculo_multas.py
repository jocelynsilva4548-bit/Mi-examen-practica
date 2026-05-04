from utils.constantes import (
    MULTA_DIARIA_ALUMNO_MXN,
    MULTA_DIARIA_PROFESOR_MXN
)


def calcular_multa_if(dias_retraso: int, tipo_usuario: str) -> float:
    """
    Calcula la multa usando la estructura clásica if/elif/else.

    >>> calcular_multa_if(0, 'alumno')
    0.0
    >>> calcular_multa_if(10, 'alumno')
    50.0
    >>> calcular_multa_if(31, 'profesor')
    74.4
    >>> calcular_multa_if(40, 'admin')
    0.0
    """
    if dias_retraso <= 0:
        return 0.0

    multa_base = 0.0

    if tipo_usuario == "alumno":
        multa_base = dias_retraso * MULTA_DIARIA_ALUMNO_MXN
    elif tipo_usuario == "profesor":
        multa_base = dias_retraso * MULTA_DIARIA_PROFESOR_MXN
    elif tipo_usuario == "admin":
        multa_base = 0.0
    else:
        # Si el tipo de usuario no es reconocido, no se cobra nada por defecto
        multa_base = 0.0

    # Aplica recargo del 20% si el retraso supera los 30 días
    if dias_retraso > 30:
        multa_base = multa_base * 1.20

    return round(multa_base, 2)


def calcular_multa_match(dias_retraso: int, tipo_usuario: str) -> float:
    """
    Calcula la multa usando la estructura moderna match/case (Python 3.10+).

    >>> calcular_multa_match(0, 'alumno')
    0.0
    >>> calcular_multa_match(10, 'alumno')
    50.0
    >>> calcular_multa_match(31, 'profesor')
    74.4
    >>> calcular_multa_match(40, 'admin')
    0.0
    """
    if dias_retraso <= 0:
        return 0.0

    multa_base = 0.0

    match tipo_usuario:
        case "alumno":
            multa_base = dias_retraso * MULTA_DIARIA_ALUMNO_MXN
        case "profesor":
            multa_base = dias_retraso * MULTA_DIARIA_PROFESOR_MXN
        case "admin":
            multa_base = 0.0
        case _:
            # El caso '_' captura cualquier cosa (equivalente a 'else')
            multa_base = 0.0

    # Aplica recargo del 20% si el retraso supera los 30 días
    if dias_retraso > 30:
        multa_base = multa_base * 1.20

    return round(multa_base, 2)


if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose=True)
