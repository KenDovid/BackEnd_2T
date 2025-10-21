# 📚 Ejercicio 36: Biblioteca con Libros y Usuarios
# Modela un sistema donde los usuarios pueden tomar prestados libros.

class Libro:
    def __init__(self, titulo):
        self.titulo = titulo
        self.disponible = True

class Usuario:
    def __init__(self, nombre):
        self.nombre = nombre
        self.prestamos = []

    def tomar_libro(self, libro):
        if libro.disponible:
            libro.disponible = False
            self.prestamos.append(libro)
            return f"{self.nombre} tomó '{libro.titulo}'."
        return f"'{libro.titulo}' no está disponible."

# Uso
libro1 = Libro("El Principito")
usuario = Usuario("Clara")
print(usuario.tomar_libro(libro1))
