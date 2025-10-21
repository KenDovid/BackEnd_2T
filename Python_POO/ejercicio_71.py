# 🏗️ Ejercicio 71: Patrón Singleton — Instancia Única Global
# Garantiza que solo exista una instancia de la clase.

class Singleton:
    __instancia = None

    def __new__(cls):
        if not cls.__instancia:
            cls.__instancia = super().__new__(cls)
        return cls.__instancia

# Uso
s1 = Singleton()
s2 = Singleton()
print(s1 is s2)  # True
