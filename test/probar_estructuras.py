from servicios.gestor_cola import GestorCola
from servicios.historial import Historial
from modelos.usuario import Alumno
from modelos.libro import LibroFisico

def probar_estructuras():
    print("=== PRUEBA DE ESTRUCTURAS DE DATOS (FIFO / LIFO) ===\n")

    # 1. Probar Cola (FIFO)
    print("--- 1. Probando Gestor de Cola (FIFO) ---")
    cola = GestorCola()
    u1 = Alumno("Alice", "alice@email.com", "101")
    u2 = Alumno("Bob", "bob@email.com", "102")
    l1 = LibroFisico("Python Pro", "A. Tutor", "1234567890123", 2021, "Tech", "A1", 1)

    cola.encolar_solicitud(u1, l1)
    cola.encolar_solicitud(u2, l1)
    print(f"Solicitudes en cola: {len(cola.ver_cola())}")

    siguiente = cola.atender_siguiente()
    if siguiente:
        print(f"Atendiendo a: {siguiente[0].nombre} para el libro {siguiente[1].titulo}")
    
    print(f"Solicitudes restantes: {len(cola.ver_cola())}\n")


    # 2. Probar Pila (LIFO)
    print("--- 2. Probando Historial (LIFO) ---")
    historial = Historial()
    
    historial.registrar_accion("Agregó libro 'Don Quijote'")
    historial.registrar_accion("Registró usuario 'Carlos'")
    historial.registrar_accion("Realizó préstamo #45")

    print(f"Acciones registradas: {len(historial.ver_historial())}")
    
    ultima = historial.deshacer_ultima()
    print(f"Deshaciendo última acción: {ultima}")
    
    print(f"Historial actual: {historial.ver_historial()}")

    print("\n=== PRUEBAS FINALIZADAS ===")

if __name__ == "__main__":
    probar_estructuras()
