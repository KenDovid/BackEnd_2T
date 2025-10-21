# 🏫 Ejercicio 14: Clase Persona y Subclase Estudiante
# Herencia con atributos y métodos adicionales para especialización.

class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def presentarse(self):
        return f"Soy {self.nombre} y tengo {self.edad} años."

class Estudiante(Persona):
    def __init__(self, nombre, edad, carrera):
        super().__init__(nombre, edad)
        self.carrera = carrera

    def estudiar(self):
        return f"{self.nombre} está estudiando {self.carrera}."

# Uso
alumno = Estudiante("Laura", 21, "Ingeniería")
print(alumno.presentarse(), alumno.estudiar())
