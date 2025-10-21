# 🐾 Ejercicio 11: Clase Animal y Subclases Perro/Gato
# Introduce la herencia. Las subclases heredan atributos y redefinen comportamientos.

class Animal:
    def __init__(self, nombre):
        self.nombre = nombre

    def hacer_sonido(self):
        return "Un animal hace un sonido."

    def moverse(self):
        return f"{self.nombre} se está moviendo."

class Perro(Animal):
    def __init__(self, nombre, raza):
        super().__init__(nombre)
        self.raza = raza

    def hacer_sonido(self):
        return "Guau, guau!"

    def ladrar(self):
        return f"{self.nombre} está ladrando."

class Gato(Animal):
    def __init__(self, nombre, color):
        super().__init__(nombre)
        self.color = color

    def hacer_sonido(self):
        return "Miau, miau."

    def maullar(self):
        return f"{self.nombre} está maullando."

# Uso
perro = Perro("Fido", "Labrador")
gato = Gato("Luna", "Negro")
print(perro.hacer_sonido(), "-", gato.hacer_sonido())
