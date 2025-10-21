# 🔒 Ejercicio 79: Manejo de Archivos con Excepciones
# Controla errores al abrir, leer o escribir archivos.

def leer_archivo(nombre):
    try:
        with open(nombre, "r") as f:
            return f.read()
    except FileNotFoundError:
        return "Archivo no encontrado."
    except Exception as e:
        return f"Error desconocido: {e}"

# Uso
print(leer_archivo("inexistente.txt"))
