# 🧠 Ejercicio 52: Mixin — Funcionalidad Extra sin Ser Clase Base Principal
# Los mixins agregan comportamiento a clases existentes sin modificar su herencia principal.

class LoggerMixin:
    def log(self, mensaje):
        print(f"[LOG]: {mensaje}")

class ServicioWeb(LoggerMixin):
    def conectar(self):
        self.log("Conectando al servidor...")
        return "Conectado exitosamente."

# Uso
servicio = ServicioWeb()
print(servicio.conectar())
