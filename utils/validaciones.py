import re
from tkinter import messagebox


def validar_isbn13(isbn: str) -> bool:
    """
    Valida que un ISBN-13 contenga 13 dígitos y que todos sean números.
    Muestra un cuadro de error si la validación falla.
    """
    # Limpiamos el ISBN de posibles guiones o espacios
    isbn_limpio = isbn.replace("-", "").replace(" ", "")

    if not isbn_limpio.isdigit() or len(isbn_limpio) != 13:
        mensaje = (
            "El ISBN proporcionado no es válido.\n"
            "Debe estar compuesto por exactamente 13 dígitos numéricos."
        )
        messagebox.showerror(title="Error en ISBN", message=mensaje)
        return False

    return True


def validar_email(email: str) -> bool:
    """
    Valida que el correo electrónico tenga un formato correcto.
    Muestra un cuadro de error si la validación falla.
    """
    # Expresión regular que verifica el formato de correo
    patron_correo = r"^[\w\.-]+@[\w\.-]+\.\w+$"

    if not re.match(patron_correo, email):
        mensaje = (
            "El formato del correo electrónico es incorrecto.\n"
            "Asegúrese de que contenga '@' y un dominio válido\n"
            "(ejemplo: usuario@correo.com)."
        )
        messagebox.showerror(
            title="Error en Correo Electrónico",
            message=mensaje
        )
        return False

    return True
