# ⚙️ Ejercicio 76: Patrón Command — Encapsular Acciones
# Cada comando ejecuta una acción específica sobre un receptor.

class Luz:
    def encender(self): return "💡 Luz encendida."
    def apagar(self): return "💡 Luz apagada."

class ComandoEncender:
    def __init__(self, luz): self.luz = luz
    def ejecutar(self): return self.luz.encender()

class ComandoApagar:
    def __init__(self, luz): self.luz = luz
    def ejecutar(self): return self.luz.apagar()

# Uso
luz = Luz()
on = ComandoEncender(luz)
off = ComandoApagar(luz)
print(on.ejecutar(), "|", off.ejecutar())
