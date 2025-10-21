# 🏢 Ejercicio 81: Relación Empresa → Empleado
# Una empresa contiene varios empleados, usando composición.

class Empleado:
    def __init__(self, nombre, puesto):
        self.nombre = nombre
        self.puesto = puesto

    def __str__(self):
        return f"{self.nombre} - {self.puesto}"

class Empresa:
    def __init__(self, nombre):
        self.nombre = nombre
        self.empleados = []

    def contratar(self, empleado):
        self.empleados.append(empleado)

    def mostrar_empleados(self):
        return [str(e) for e in self.empleados]

# Uso
empresa = Empresa("TechCorp")
empresa.contratar(Empleado("Ana", "Desarrolladora"))
empresa.contratar(Empleado("Luis", "Diseñador"))
print(empresa.mostrar_empleados())
