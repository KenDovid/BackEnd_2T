# 🛍️ Ejercicio 92: E-Commerce Simplificado
# Productos, carrito y cálculo total con descuentos.

class Producto:
    def __init__(self, nombre, precio):
        self.nombre = nombre
        self.precio = precio

class Carrito:
    def __init__(self):
        self.items = []

    def agregar(self, producto):
        self.items.append(producto)

    def total(self, descuento=0):
        subtotal = sum(p.precio for p in self.items)
        return subtotal * (1 - descuento / 100)

# Uso
c = Carrito()
c.agregar(Producto("Laptop", 1200))
c.agregar(Producto("Mouse", 50))
print("Total con 10% de descuento:", c.total(10))
