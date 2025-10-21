# 🧮 Ejercicio 58: Mixin Matemático — Promedio Automático
# Agrega a cualquier clase la habilidad de calcular promedios.

class PromedioMixin:
    def promedio(self, datos):
        return sum(datos) / len(datos) if datos else 0

class Curso(PromedioMixin):
    def __init__(self, nombre, notas):
        self.nombre = nombre
        self.notas = notas

    def promedio_final(self):
        return self.promedio(self.notas)

# Uso
curso = Curso("Matemáticas", [90, 85, 80])
print(f"Promedio de {curso.nombre}: {curso.promedio_final():.2f}")
