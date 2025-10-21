# 🔄 Ejercicio 75: Patrón Decorator — Añadir Funcionalidades Dinámicamente
# Envuelve objetos para extender su comportamiento sin modificar la clase base.

class Mensaje:
    def mostrar(self): return "Mensaje base."

class DecoradorMayusculas:
    def __init__(self, mensaje): self.mensaje = mensaje
    def mostrar(self): return self.mensaje.mostrar().upper()

class DecoradorSignos:
    def __init__(self, mensaje): self.mensaje = mensaje
    def mostrar(self): return f"*** {self.mensaje.mostrar()} ***"

# Uso
m = Mensaje()
decorado = DecoradorSignos(DecoradorMayusculas(m))
print(decorado.mostrar())
