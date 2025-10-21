# 🧠 Ejercicio 57: Mixin de Serialización — Convertir a Diccionario
# Permite que cualquier clase convierta sus atributos a formato dict fácilmente.

class SerializableMixin:
    def to_dict(self):
        return self.__dict__

class Usuario(SerializableMixin):
    def __init__(self, nombre, rol):
        self.nombre = nombre
        self.rol = rol

# Uso
u = Usuario("María", "Admin")
print(u.to_dict())
