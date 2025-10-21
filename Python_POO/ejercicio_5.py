# 🛒 Ejercicio 5: Clase Producto de Tienda
# Simula un producto con nombre, precio y stock, permitiendo actualizarlo y calcular el valor total.

class Producto:
    def __init__(self, nombre, precio, stock):
        self.nombre = nombre
        self.precio = precio
        self.stock = stock

    def mostrar_info(self):
        return f"{self.nombre} - ${self.precio:.2f} | Stock: {self.stock}"

    def actualizar_stock(self, cantidad):
        self.stock += cantidad
        return f"Nuevo stock de {self.nombre}: {self.stock}"

    def calcular_valor_total(self, unidades):
        if unidades <= self.stock:
            return f"Total: ${unidades * self.precio:.2f}"
        return "Stock insuficiente."

# Uso
laptop = Producto("Laptop Gaming", 1200, 10)
print(laptop.mostrar_info())
print(laptop.calcular_valor_total(3))
