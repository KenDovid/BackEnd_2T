# 🧮 Ejercicio 29: Propiedades Calculadas — Rectángulo Dinámico
# Usa @property para calcular área y perímetro automáticamente.

class Rectangulo:
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura

    @property
    def area(self):
        return self.base * self.altura

    @property
    def perimetro(self):
        return 2 * (self.base + self.altura)

# Uso
r = Rectangulo(10, 5)
print("Área:", r.area, "Perímetro:", r.perimetro)
