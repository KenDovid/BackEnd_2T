# 🧳 Ejercicio 30: Clases Abstractas Simples con abc
# Define una interfaz base que obliga a implementar un método.

from abc import ABC, abstractmethod

class Transporte(ABC):
    @abstractmethod
    def mover(self):
        pass

class Auto(Transporte):
    def mover(self):
        return "El auto se desplaza por carretera."

class Barco(Transporte):
    def mover(self):
        return "El barco navega por el mar."

# Uso
for t in [Auto(), Barco()]:
    print(t.mover())
