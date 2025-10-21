# 🏥 Ejercicio 19: Herencia y Validación — Clase Persona y Doctor
# Muestra cómo una subclase puede agregar validaciones específicas.

class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

class Doctor(Persona):
    def __init__(self, nombre, edad, especialidad):
        super().__init__(nombre, edad)
        self.especialidad = especialidad

    def atender_paciente(self, nombre_paciente):
        return f"Dr. {self.nombre} ({self.especialidad}) atiende a {nombre_paciente}."

# Uso
doc = Doctor("Ramírez", 45, "Cardiología")
print(doc.atender_paciente("Lucía"))
