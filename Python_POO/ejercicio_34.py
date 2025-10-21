# 🧱 Ejercicio 34: Clase Singleton — Configuración Global
# Implementa un patrón Singleton para que solo exista una instancia.

class Configuracion:
    __instancia = None

    def __new__(cls, *args, **kwargs):
        if not cls.__instancia:
            cls.__instancia = super().__new__(cls)
        return cls.__instancia

    def __init__(self, tema="Claro", idioma="ES"):
        self.tema = tema
        self.idioma = idioma

# Uso
c1 = Configuracion()
c2 = Configuracion()
print(c1 is c2)  # True
