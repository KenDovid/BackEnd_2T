# 🧱 Ejercicio 15: Herencia Multinivel con SerVivo → Animal → Mamífero → Perro
# Demuestra cómo una clase puede heredar de una cadena de antecesores.

class SerVivo:
    def respirar(self):
        return "El ser vivo respira."

class Animal(SerVivo):
    def moverse(self):
        return "El animal se mueve."

class Mamifero(Animal):
    def amamantar(self):
        return "El mamífero alimenta a sus crías."

class Perro(Mamifero):
    def ladrar(self):
        return "¡Guau!"

# Uso
rex = Perro()
print(rex.respirar(), rex.moverse(), rex.ladrar())
