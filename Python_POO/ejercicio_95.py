# 🧮 Ejercicio 95: Sistema de Evaluación Escolar
# Califica estudiantes y genera reportes de promedio.

class Estudiante:
    def __init__(self, nombre):
        self.nombre = nombre
        self.notas = []

    def agregar_nota(self, nota):
        self.notas.append(nota)

    def promedio(self):
        return sum(self.notas) / len(self.notas) if self.notas else 0

class Escuela:
    def __init__(self):
        self.estudiantes = []

    def registrar(self, estudiante):
        self.estudiantes.append(estudiante)

    def reporte(self):
        return {e.nombre: e.promedio() for e in self.estudiantes}

# Uso
e1 = Estudiante("Ana")
e1.agregar_nota(90)
e1.agregar_nota(80)
escuela = Escuela()
escuela.registrar(e1)
print(escuela.reporte())
