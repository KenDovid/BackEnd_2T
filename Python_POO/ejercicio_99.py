# 🧾 Ejercicio 99: Sistema de Contabilidad
# Maneja ingresos, gastos y calcula el balance total.

class Transaccion:
    def __init__(self, descripcion, monto):
        self.descripcion = descripcion
        self.monto = monto

class Contabilidad:
    def __init__(self):
        self.transacciones = []

    def agregar(self, transaccion):
        self.transacciones.append(transaccion)

    def balance(self):
        return sum(t.monto for t in self.transacciones)

# Uso
c = Contabilidad()
c.agregar(Transaccion("Ingreso", 500))
c.agregar(Transaccion("Gasto", -200))
print("Balance final:", c.balance())
