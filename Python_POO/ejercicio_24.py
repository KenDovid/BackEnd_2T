# 💻 Ejercicio 24: Polimorfismo con Clases de Empleado
# Cada tipo de empleado calcula su salario de forma distinta.

class Empleado:
    def calcular_pago(self):
        pass

class EmpleadoTiempoCompleto(Empleado):
    def __init__(self, salario_mensual):
        self.salario_mensual = salario_mensual

    def calcular_pago(self):
        return self.salario_mensual

class EmpleadoPorHoras(Empleado):
    def __init__(self, horas, tarifa):
        self.horas = horas
        self.tarifa = tarifa

    def calcular_pago(self):
        return self.horas * self.tarifa

# Uso
empleados = [EmpleadoTiempoCompleto(3000), EmpleadoPorHoras(80, 20)]
for e in empleados:
    print("Pago:", e.calcular_pago())
