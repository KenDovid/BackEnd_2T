# 💾 Ejercicio 85: Relación Usuario → Historial
# Cada usuario tiene su propio registro de acciones realizadas.

class Historial:
    def __init__(self):
        self.acciones = []

    def registrar(self, accion):
        self.acciones.append(accion)

class Usuario:
    def __init__(self, nombre):
        self.nombre = nombre
        self.historial = Historial()

    def hacer_accion(self, accion):
        self.historial.registrar(accion)
        return f"{self.nombre} realizó: {accion}"

# Uso
u = Usuario("Pedro")
print(u.hacer_accion("Inicio sesión"))
print(u.historial.acciones)
