# 🧭 Ejercicio 31: Clases Abstractas — Animales con Métodos Obligatorios
# Define una jerarquía en la que cada animal debe implementar “hablar” y “moverse”.

from abc import ABC, abstractmethod

class Animal(ABC):
    @abstractmethod
    def hablar(self):
        pass

    @abstractmethod
    def moverse(self):
        pass

class Perro(Animal):
    def hablar(self):
        return "Guau!"
    def moverse(self):
        return "Corre sobre cuatro patas."

class Pajaro(Animal):
    def hablar(self):
        return "Pío!"
    def moverse(self):
        return "Vuela por el cielo."

# Uso
animales = [Perro(), Pajaro()]
for a in animales:
    print(f"{a.__class__.__name__}: {a.hablar()} - {a.moverse()}")
