# 🚚 Ejercicio 83: Pedido y Producto — Relación de Agregación
# Un pedido agrupa productos pero estos pueden existir sin él.

class Producto:
    def __init__(self, nombre, precio):
        self.nombre = nombre
        self.precio = precio

class Pedido:
    def __init__(self, id_pedido):
        self.id_pedido = id_pedido
        self.productos = []

    def agregar_producto(self, producto):
        self.productos.append(producto)

    def total(self):
        return sum(p.precio for p in self.productos)

# Uso
p1 = Producto("Mouse", 40)
p2 = Producto("Teclado", 80)
pedido = Pedido(1001)
pedido.agregar_producto(p1)
pedido.agregar_producto(p2)
print("Total del pedido:", pedido.total())
