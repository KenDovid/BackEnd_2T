# 🧮 Ejercicio 69: Métodos de Clase + Estático Combinados
# Combina ambos para manejar y validar datos de forma estructurada.

class Usuario:
    usuarios = []

    def __init__(self, nombre):
        self.nombre = nombre
        Usuario.usuarios.append(nombre)

    @classmethod
    def total(cls):
        return len(cls.usuarios)

    @staticmethod
    def validar_nombre(nombre):
        return nombre.isalpha()

# Uso
Usuario("Ana")
Usuario("Pedro")
print("Total usuarios:", Usuario.total())
print("¿Nombre válido?", Usuario.validar_nombre("Carlos"))
