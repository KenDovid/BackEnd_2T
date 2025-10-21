# 🧠 Ejercicio 67: Métodos Especiales — __repr__ y __str__
# Diferencia entre representaciones técnicas y legibles.

class Libro:
    def __init__(self, titulo, autor):
        self.titulo = titulo
        self.autor = autor

    def __repr__(self):
        return f"Libro('{self.titulo}', '{self.autor}')"

    def __str__(self):
        return f"'{self.titulo}' por {self.autor}"

# Uso
l = Libro("1984", "George Orwell")
print(repr(l))
print(str(l))
