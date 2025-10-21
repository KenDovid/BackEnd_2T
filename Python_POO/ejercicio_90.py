# ⚙️ Ejercicio 90: Sistema de Biblioteca Avanzado
# Combina usuarios, libros y préstamos con relaciones cruzadas.

class Libro:
    def __init__(self, titulo):
        self.titulo = titulo
        self.disponible = True

class Usuario:
    def __init__(self, nombre):
        self.nombre = nombre
        self.prestamos = []

class Prestamo:
    def __init__(self, usuario, libro):
        self.usuario = usuario
        self.libro = libro
        libro.disponible = False
        usuario.prestamos.append(self)

# Uso
libro = Libro("1984")
usuario = Usuario("Marta")
Prestamo(usuario, libro)
print(f"{usuario.nombre} tomó '{libro.titulo}' — Disponible: {libro.disponible}")
