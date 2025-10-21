# 🔺 Ejercicio 9: Clase Rectángulo con Área y Perímetro
# Calcula el área y perímetro a partir de sus dimensiones.

class Rectangulo:
    def __init__(self, largo, ancho):
        if largo <= 0 or ancho <= 0:
            raise ValueError("Dimensiones inválidas.")
        self.largo = largo
        self.ancho = ancho

    def area(self):
        return self.largo * self.ancho

    def perimetro(self):
        return 2 * (self.largo + self.ancho)

# Uso
rect = Rectangulo(10, 5)
print("Área:", rect.area())
print("Perímetro:", rect.perimetro())
