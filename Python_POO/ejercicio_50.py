# 🧬 Ejercicio 50: Contador de Objetos Instanciados
# Usa una variable de clase para contar cuántas instancias existen.

class Usuario:
    cantidad = 0

    def __init__(self, nombre):
        self.nombre = nombre
        Usuario.cantidad += 1

    @classmethod
    def total_usuarios(cls):
        return f"Usuarios creados: {cls.cantidad}"

# Uso
u1 = Usuario("Ana")
u2 = Usuario("Pedro")
print(Usuario.total_usuarios())
