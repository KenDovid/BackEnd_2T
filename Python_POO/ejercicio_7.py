# 📚 Ejercicio 7: Clase Libro con Estado de Préstamo
# Simula una biblioteca donde los libros pueden prestarse y devolverse.

class Libro:
    def __init__(self, titulo, autor):
        self.titulo = titulo
        self.autor = autor
        self.disponible = True

    def prestar(self):
        if self.disponible:
            self.disponible = False
            return f"'{self.titulo}' ha sido prestado."
        return f"'{self.titulo}' no está disponible."

    def devolver(self):
        if not self.disponible:
            self.disponible = True
            return f"'{self.titulo}' ha sido devuelto."
        return f"'{self.titulo}' ya está en la biblioteca."

# Uso
libro = Libro("Cien años de soledad", "G. G. Márquez")
print(libro.prestar())
print(libro.devolver())
