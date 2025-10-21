# 🧮 Ejercicio 39: Clases con Métodos de Clase — Contador de Instancias
# Usa @classmethod para contar cuántos objetos se han creado.

class Contador:
    total = 0

    def __init__(self):
        Contador.total += 1

    @classmethod
    def mostrar_total(cls):
        return f"Se han creado {cls.total} instancias."

# Uso
a, b, c = Contador(), Contador(), Contador()
print(Contador.mostrar_total())
