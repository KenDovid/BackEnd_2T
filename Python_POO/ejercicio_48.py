# 🧩 Ejercicio 48: Composición Avanzada — Computadora con Componentes
# Cada parte es un objeto, y la computadora los agrupa todos.

class CPU:
    def __init__(self, modelo):
        self.modelo = modelo

class RAM:
    def __init__(self, capacidad):
        self.capacidad = capacidad

class Computadora:
    def __init__(self, cpu, ram):
        self.cpu = cpu
        self.ram = ram

    def especificaciones(self):
        return f"CPU: {self.cpu.modelo}, RAM: {self.ram.capacidad} GB"

# Uso
pc = Computadora(CPU("Intel i7"), RAM(16))
print(pc.especificaciones())
