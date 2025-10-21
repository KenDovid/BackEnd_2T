# 💼 Ejercicio 13: Clase Empleado y Subclases Gerente/Desarrollador
# Modela una jerarquía laboral con diferentes bonificaciones.

class Empleado:
    def __init__(self, nombre, salario):
        self.nombre = nombre
        self.salario = salario

    def salario_anual(self):
        return self.salario * 12

class Gerente(Empleado):
    def __init__(self, nombre, salario, departamento):
        super().__init__(nombre, salario)
        self.departamento = departamento

    def calcular_bonus(self):
        return self.salario * 0.15

class Desarrollador(Empleado):
    def __init__(self, nombre, salario, lenguaje):
        super().__init__(nombre, salario)
        self.lenguaje = lenguaje

    def calcular_bonus(self):
        return self.salario * 0.10

# Uso
gerente = Gerente("Lucía", 4000, "Ventas")
dev = Desarrollador("Pablo", 3500, "Python")
print(gerente.calcular_bonus(), "-", dev.calcular_bonus())
