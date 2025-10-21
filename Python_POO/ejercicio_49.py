# 🧱 Ejercicio 49: Contenedor Personalizado — Carrito de Compras
# Permite agregar y mostrar productos como una lista interna.

class Carrito:
    def __init__(self):
        self.items = []

    def agregar(self, producto):
        self.items.append(producto)

    def __len__(self):
        return len(self.items)

    def __iter__(self):
        return iter(self.items)

# Uso
carrito = Carrito()
carrito.agregar("Laptop")
carrito.agregar("Mouse")
print("Productos en carrito:", len(carrito))
for i in carrito:
    print("-", i)
