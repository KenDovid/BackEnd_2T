# 🧬 Ejercicio 17: Clase Animal con Subclases Ave y Pez
# Cada subclase redefine métodos según su naturaleza.

class Animal:
    def __init__(self, nombre):
        self.nombre = nombre

    def moverse(self):
        return "El animal se mueve."

class Ave(Animal):
    def moverse(self):
        return f"{self.nombre} vuela alto."

class Pez(Animal):
    def moverse(self):
        return f"{self.nombre} nada rápido."

# Uso
ave = Ave("Águila")
pez = Pez("Nemo")
print(ave.moverse(), "-", pez.moverse())
