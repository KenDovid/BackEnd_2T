# 🏗️ Ejercicio 20: Herencia en la Construcción — Clase Edificio y Subclases
# Modela una jerarquía con atributos específicos según el tipo de edificio.

class Edificio:
    def __init__(self, nombre, pisos):
        self.nombre = nombre
        self.pisos = pisos

class Escuela(Edificio):
    def __init__(self, nombre, pisos, aulas):
        super().__init__(nombre, pisos)
        self.aulas = aulas

    def info(self):
        return f"{self.nombre}: {self.pisos} pisos, {self.aulas} aulas."

class Hospital(Edificio):
    def __init__(self, nombre, pisos, camas):
        super().__init__(nombre, pisos)
        self.camas = camas

    def info(self):
        return f"{self.nombre}: {self.pisos} pisos, {self.camas} camas disponibles."

# Uso
escuela = Escuela("Colegio Central", 3, 25)
hospital = Hospital("Clínica Vida", 5, 120)
print(escuela.info(), "|", hospital.info())
