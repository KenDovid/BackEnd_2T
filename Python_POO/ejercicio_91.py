# 💼 Ejercicio 91: Sistema de Gestión de Tareas
# Cada tarea tiene estado y prioridad; un gestor las administra.

class Tarea:
    def __init__(self, descripcion, prioridad):
        self.descripcion = descripcion
        self.prioridad = prioridad
        self.completada = False

    def marcar_completada(self):
        self.completada = True

class GestorTareas:
    def __init__(self):
        self.tareas = []

    def agregar_tarea(self, tarea):
        self.tareas.append(tarea)

    def pendientes(self):
        return [t.descripcion for t in self.tareas if not t.completada]

# Uso
g = GestorTareas()
g.agregar_tarea(Tarea("Aprender POO", "Alta"))
g.agregar_tarea(Tarea("Dormir", "Baja"))
print("Pendientes:", g.pendientes())
