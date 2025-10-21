# 🧩 Ejercicio 41: Método __str__ — Representación Amigable
# Permite que los objetos se muestren de forma legible al imprimirlos.

class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def __str__(self):
        return f"{self.nombre}, {self.edad} años"

# Uso
p = Persona("Carlos", 28)
print(p)  # Llama automáticamente a __str__
