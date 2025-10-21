# 🧰 Ejercicio 59: Mixin de Logging Avanzado
# Añade un sistema de registro que guarda en lista los eventos.

class LogMixin:
    def __init__(self):
        self.logs = []

    def registrar(self, mensaje):
        self.logs.append(mensaje)

class Sistema(LogMixin):
    def __init__(self, nombre):
        super().__init__()
        self.nombre = nombre

    def ejecutar(self, tarea):
        self.registrar(f"Ejecutando {tarea}")
        return f"{self.nombre}: {tarea} completada."

# Uso
s = Sistema("Backend")
print(s.ejecutar("Backup"))
print(s.logs)
