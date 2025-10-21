# 🎓 Ejercicio 6: Clase Estudiante con Calificaciones
# Gestiona una lista de notas y calcula el promedio.

class Estudiante:
    def __init__(self, nombre, id_estudiante):
        self.nombre = nombre
        self.id = id_estudiante
        self.calificaciones = []

    def agregar_calificacion(self, nota):
        if 0 <= nota <= 100:
            self.calificaciones.append(nota)
            return f"Nota {nota} agregada."
        return "Calificación inválida."

    def obtener_promedio(self):
        if not self.calificaciones:
            return 0
        return sum(self.calificaciones) / len(self.calificaciones)

# Uso
alumno = Estudiante("Ana", "E101")
alumno.agregar_calificacion(85)
alumno.agregar_calificacion(90)
print(f"Promedio: {alumno.obtener_promedio():.2f}")
