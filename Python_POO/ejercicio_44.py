# 🧠 Ejercicio 44: Método __add__ — Sumar Objetos Personalizados
# Permite combinar objetos con el operador “+”.

class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, otro):
        return Vector(self.x + otro.x, self.y + otro.y)

    def __str__(self):
        return f"({self.x}, {self.y})"

# Uso
v1 = Vector(3, 4)
v2 = Vector(1, 2)
print(v1 + v2)
