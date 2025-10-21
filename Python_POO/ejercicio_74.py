# 🧩 Ejercicio 74: Patrón Strategy — Comportamiento Intercambiable
# Permite cambiar el algoritmo de ejecución dinámicamente.

class EstrategiaSuma:
    def ejecutar(self, a, b): return a + b

class EstrategiaResta:
    def ejecutar(self, a, b): return a - b

class Calculadora:
    def __init__(self, estrategia):
        self.estrategia = estrategia

    def operar(self, a, b):
        return self.estrategia.ejecutar(a, b)

# Uso
calc = Calculadora(EstrategiaSuma())
print("Suma:", calc.operar(5, 3))
calc.estrategia = EstrategiaResta()
print("Resta:", calc.operar(5, 3))
