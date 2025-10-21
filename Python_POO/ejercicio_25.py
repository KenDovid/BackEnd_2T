# 🎨 Ejercicio 25: Polimorfismo — Figuras Geométricas
# Cada figura implementa el cálculo del área a su manera.

class Figura:
    def area(self):
        pass

class Cuadrado(Figura):
    def __init__(self, lado):
        self.lado = lado
    def area(self):
        return self.lado ** 2

class Circulo(Figura):
    def __init__(self, radio):
        self.radio = radio
    def area(self):
        return 3.1416 * self.radio ** 2

# Uso
formas = [Cuadrado(4), Circulo(3)]
for f in formas:
    print(f"{f.__class__.__name__} área: {f.area():.2f}")
