# ⚖️ Ejercicio 42: Métodos de Comparación (__eq__, __lt__)
# Permite comparar objetos como si fueran valores numéricos o cadenas.

class Producto:
    def __init__(self, nombre, precio):
        self.nombre = nombre
        self.precio = precio

    def __eq__(self, otro):
        return self.precio == otro.precio

    def __lt__(self, otro):
        return self.precio < otro.precio

# Uso
p1 = Producto("Teclado", 50)
p2 = Producto("Mouse", 30)
print(p1 > p2, p1 == p2)
