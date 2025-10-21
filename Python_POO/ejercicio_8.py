# 👔 Ejercicio 8: Clase Empleado con Salario y Aumentos
# Calcula salario anual y permite aplicar aumentos porcentuales.

class Empleado:
    def __init__(self, nombre, puesto, salario_mensual):
        self.nombre = nombre
        self.puesto = puesto
        self.salario_mensual = salario_mensual

    def obtener_salario_anual(self):
        return self.salario_mensual * 12

    def aplicar_aumento(self, porcentaje):
        if 0 < porcentaje <= 100:
            self.salario_mensual *= (1 + porcentaje / 100)
            return f"Nuevo salario: ${self.salario_mensual:.2f}"
        return "Porcentaje inválido."

# Uso
emp = Empleado("Carlos", "Desarrollador", 3000)
print(emp.aplicar_aumento(10))
print(emp.obtener_salario_anual())
