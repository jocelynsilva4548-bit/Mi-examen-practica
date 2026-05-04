# constantes.py
# Definición de constantes globales para el Sistema de Gestión de Biblioteca Digital

# Límite máximo de libros que pueden tener en préstamo simultáneamente
MAXIMO_LIBROS_PROFESORES = 10
MAXIMO_LIBROS_ALUMNOS = 3

# Multa monetaria por cada día de retraso en la devolución (en Pesos Mexicanos - MXN)
MULTA_DIARIA_ALUMNO_MXN = 5.00
MULTA_DIARIA_PROFESOR_MXN = 2.00

# Estados posibles en los que puede encontrarse un libro
ESTADO_DISPONIBLE = "DISPONIBLE"
ESTADO_PRESTADO = "PRESTADO"

# Formatos válidos (Soportan tanto formato físico como extensiones digitales)
FORMATOS_VALIDOS = ["FÍSICO", ".pdf", ".epub", ".docx", ".txt"]
