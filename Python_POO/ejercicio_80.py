# 🧾 Ejercicio 80: Uso de finally — Limpieza de Recursos
# Asegura que ciertas acciones se ejecuten siempre, incluso si hay error.

def procesar_datos():
    try:
        print("Procesando datos...")
        1 / 0  # Error forzado
    except ZeroDivisionError:
        print("Error de división detectado.")
    finally:
        print("Cerrando conexión y limpiando recursos...")

# Uso
procesar_datos()
