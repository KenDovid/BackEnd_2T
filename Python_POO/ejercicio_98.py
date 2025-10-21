# 💻 Ejercicio 98: Sistema de Cursos Online
# Estudiantes se inscriben a cursos y cada curso almacena sus inscritos.

class Curso:
    def __init__(self, titulo):
        self.titulo = titulo
        self.inscritos = []

class Estudiante:
    def __init__(self, nombre):
        self.nombre = nombre
        self.cursos = []

    def inscribirse(self, curso):
        curso.inscritos.append(self)
        self.cursos.append(curso)

# Uso
curso = Curso("Python Intermedio")
alumno = Estudiante("Carlos")
alumno.inscribirse(curso)
print(f"{alumno.nombre} inscrito en {[c.titulo for c in alumno.cursos]}")
