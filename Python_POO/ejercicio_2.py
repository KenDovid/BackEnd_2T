# 🧮 Ejercicio 2: Clase Calculadora
# Implementa una calculadora con operaciones básicas: suma, resta, multiplicación y división.

class Calculadora:
    def sumar(self, a, b):
        return a + b

    def restar(self, a, b):
        return a - b

    def multiplicar(self, a, b):
        return a * b

    def dividir(self, a, b):
        return a / b if b != 0 else "Error: División por cero."

# Uso
calc = Calculadora()
print(calc.sumar(5, 3))
print(calc.dividir(10, 0))
