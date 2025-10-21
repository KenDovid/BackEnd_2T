# 🧾 Ejercicio 82: Sistema de Facturas y Clientes
# Cada cliente puede tener varias facturas asociadas.

class Factura:
    def __init__(self, numero, total):
        self.numero = numero
        self.total = total

class Cliente:
    def __init__(self, nombre):
        self.nombre = nombre
        self.facturas = []

    def agregar_factura(self, factura):
        self.facturas.append(factura)

    def total_gastado(self):
        return sum(f.total for f in self.facturas)

# Uso
cliente = Cliente("Sofía")
cliente.agregar_factura(Factura(1, 250))
cliente.agregar_factura(Factura(2, 180))
print("Total gastado:", cliente.total_gastado())
