# 🎨 Ejercicio 66: Sobrecarga de Operadores — Multiplicación Personalizada
# Permite multiplicar objetos personalizados con un operador.

class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __mul__(self, escalar):
        return Vector(self.x * escalar, self.y * escalar)

    def __repr__(self):
        return f"Vector({self.x}, {self.y})"

# Uso
v = Vector(3, 4)
print(v * 2)
