# 🎭 Ejercicio 61: Método __call__ — Objetos que se Comportan como Funciones
# Permite que una instancia sea llamada directamente como si fuera una función.

class ContadorLlamadas:
    def __init__(self):
        self.total = 0

    def __call__(self):
        self.total += 1
        return f"Llamada número {self.total}"

# Uso
contador = ContadorLlamadas()
print(contador())
print(contador())
