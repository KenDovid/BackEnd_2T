# 🧾 Ejercicio 32: Sistema de Facturación con Clases Abstractas
# Cada tipo de factura implementa su método para calcular total.

from abc import ABC, abstractmethod

class Factura(ABC):
    @abstractmethod
    def calcular_total(self):
        pass

class FacturaSimple(Factura):
    def __init__(self, subtotal):
        self.subtotal = subtotal
    def calcular_total(self):
        return self.subtotal * 1.19  # IVA 19%

class FacturaDescuento(Factura):
    def __init__(self, subtotal, descuento):
        self.subtotal = subtotal
        self.descuento = descuento
    def calcular_total(self):
        return (self.subtotal - self.descuento) * 1.19

# Uso
f1 = FacturaSimple(100)
f2 = FacturaDescuento(200, 20)
print("Totales:", f1.calcular_total(), f2.calcular_total())
