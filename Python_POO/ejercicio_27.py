# 🧩 Ejercicio 27: Polimorfismo con Animales
# Mismo método, diferentes resultados según el tipo de animal.

class Animal:
    def hablar(self):
        pass

class Perro(Animal):
    def hablar(self):
        return "¡Guau!"

class Gato(Animal):
    def hablar(self):
        return "¡Miau!"

class Vaca(Animal):
    def hablar(self):
        return "¡Muuu!"

# Uso
for animal in [Perro(), Gato(), Vaca()]:
    print(f"{animal.__class__.__name__} dice: {animal.hablar()}")
