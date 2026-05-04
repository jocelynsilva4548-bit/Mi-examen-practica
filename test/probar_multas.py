from servicios.calculo_multas import calcular_multa_match as calcular_multa


def probar_escenarios():
    """Ejecuta múltiples pruebas manuales e imprime los resultados en consola."""
    print("--- INICIANDO PRUEBAS DE CÁLCULO DE MULTAS ---\n")

    # Caso 1: Sin retraso (0 días)
    resultado1 = calcular_multa(0, "alumno")
    print(f"Caso 1 - Alumno sin retraso (0 días): ${resultado1} (Esperado: $0.0)")

    # Caso 2: Alumno con retraso normal (10 días)
    # Cálculo: 10 * $5 = $50.0
    resultado2 = calcular_multa(10, "alumno")
    print(f"Caso 2 - Alumno con retraso de 10 días: ${resultado2} (Esperado: $50.0)")

    # Caso 3: Profesor con retraso mayor a 30 días (31 días, aplica recargo 20%)
    # Cálculo: 31 * $2 = $62 + 20% = $74.4
    resultado3 = calcular_multa(31, "profesor")
    print(f"Caso 3 - Profesor con retraso de 31 días: ${resultado3} (Esperado: $74.4)")

    # Caso 4: Administrador (cualquier cantidad de días, la multa siempre es 0)
    resultado4 = calcular_multa(40, "admin")
    print(f"Caso 4 - Admin con retraso de 40 días: ${resultado4} (Esperado: $0.0)")

    # Caso 5: Usuario inexistente o no reconocido ("visitante")
    # Cálculo: Por defecto no se cobra nada si el tipo no está en las reglas
    resultado5 = calcular_multa(15, "visitante")
    print(f"Caso 5 - Usuario inexistente (15 días): ${resultado5} (Esperado: $0.0)")

    # Caso 6: Alumno con retraso mayor a 30 días (40 días, aplica recargo 20%)
    # Cálculo: 40 * $5 = $200 + 20% = $240.0
    resultado6 = calcular_multa(40, "alumno")
    print(f"Caso 6 - Alumno con retraso de 40 días: ${resultado6} (Esperado: $240.0)")

    print("\n--- PRUEBAS FINALIZADAS ---")


if __name__ == "__main__":
    probar_escenarios()
