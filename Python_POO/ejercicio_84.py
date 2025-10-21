# 🧠 Ejercicio 84: Asociación Bidireccional — Profesor y Curso
# Un profesor puede dictar varios cursos, y cada curso conoce a su profesor.

class Profesor:
    def __init__(self, nombre):
        self.nombre = nombre
        self.cursos = []

    def asignar_curso(self, curso):
        self.cursos.append(curso)
        curso.profesor = self

class Curso:
    def __init__(self, nombre):
        self.nombre = nombre
        self.profesor = None

# Uso
p = Profesor("Laura")
c1 = Curso("Python")
c2 = Curso("IA")
p.asignar_curso(c1)
p.asig
