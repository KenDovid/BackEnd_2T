# 🐾 Ejercicio 10: Clase Mascota con Estados de Ánimo
# Cambia el estado emocional según las acciones (alimentar, jugar, dormir).

class Mascota:
    def __init__(self, nombre, especie):
        self.nombre = nombre
        self.especie = especie
        self.estado = "Feliz"

    def alimentar(self):
        self.estado = "Satisfecho"
        return f"{self.nombre} está {self.estado}."

    def jugar(self):
        self.estado = "Animado"
        return f"{self.nombre} está {self.estado}."

    def dormir(self):
        self.estado = "Durmiendo"
        return f"{self.nombre} está {self.estado}."

# Uso
perro = Mascota("Max", "Perro")
print(perro.jugar())
print(perro.dormir())
