# 💡 Ejercicio 68: Propiedades Dinámicas con @property
# Usa @property para definir atributos calculados en tiempo real.

class Triangulo:
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura

    @property
    def area(self):
        return (self.base * self.altura) / 2

# Uso
t = Triangulo(10, 6)
print(f"Área: {t.area}")
