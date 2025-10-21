# 📦 Ejercicio 35: Sistema de Inventario
# Usa una clase para manejar una lista de productos y sus existencias.

class Producto:
    def __init__(self, nombre, cantidad):
        self.nombre = nombre
        self.cantidad = cantidad

class Inventario:
    def __init__(self):
        self.productos = []

    def agregar_producto(self, producto):
        self.productos.append(producto)

    def mostrar_inventario(self):
        return [f"{p.nombre}: {p.cantidad} unidades" for p in self.productos]

# Uso
inv = Inventario()
inv.agregar_producto(Producto("Tornillos", 150))
inv.agregar_producto(Producto("Tuercas", 300))
print(inv.mostrar_inventario())
