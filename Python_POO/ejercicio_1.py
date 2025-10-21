# 🧩 Ejercicio 1: Clase Persona Básica
# Crea una clase Persona con nombre y edad, que permita saludar y cumplir años.

class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def saludar(self):
        return f"Hola, mi nombre es {self.nombre}."

    def cumplir_anios(self):
        self.edad += 1
        return f"¡Feliz cumpleaños, {self.nombre}! Ahora tienes {self.edad} años."

# Uso
persona1 = Persona("Ana", 30)
print(persona1.saludar())
print(persona1.cumplir_anios())
