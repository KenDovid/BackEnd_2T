# 📦 Ejercicio 86: Tienda con Inventario y Ventas
# Modela un sistema simple de ventas y control de stock.

class Producto:
    def __init__(self, nombre, stock, precio):
        self.nombre = nombre
        self.stock = stock
        self.precio = precio

class Tienda:
    def __init__(self):
        self.productos = []

    def agregar_producto(self, producto):
        self.productos.append(producto)

    def vender(self, nombre, cantidad):
        for p in self.productos:
            if p.nombre == nombre:
                if p.stock >= cantidad:
                    p.stock -= cantidad
                    return f"Venta exitosa: {cantidad} {p.nombre}(s) vendidos."
                else:
                    return "Stock insuficiente."
        return "Producto no encontrado."

# Uso
t = Tienda()
t.agregar_producto(Producto("Camisa", 10, 20))
print(t.vender("Camisa", 3))
