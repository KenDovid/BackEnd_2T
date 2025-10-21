# 🧱 Ejercicio 89: Sistema Escolar — Escuela, Estudiantes y Cursos
# Un modelo modular donde múltiples relaciones coexisten.

class Estudiante:
    def __init__(self, nombre):
        self.nombre = nombre
        self.cursos = []

class Curso:
    def __init__(self, nombre):
        self.nombre = nombre
        self.estudiantes = []

class Escuela:
    def __init__(self, nombre):
        self.nombre = nombre
        self.cursos = []

    def agregar_curso(self, curso):
        self.cursos.append(curso)

# Uso
e1 = Estudiante("Juan")
c1 = Curso("Matemáticas")
c1.estudiantes.append(e1)
escuela = Escuela("Colegio Moderno")
escuela.agregar_curso(c1)
print(f"{e1.nombre} estudia {c1.nombre} en {escuela.nombre}")
