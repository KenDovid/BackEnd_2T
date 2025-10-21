# 🧮 Ejercicio 33: Clase Calculadora con Métodos Estáticos
# Usa métodos estáticos para operaciones que no dependen del estado de un objeto.

class Calculadora:
    @staticmethod
    def sumar(a, b):
        return a + b

    @staticmethod
    def restar(a, b):
        return a - b

    @staticmethod
    def multiplicar(a, b):
        return a * b

    @staticmethod
    def dividir(a, b):
        return a / b if b != 0 else "Error: división por cero."

# Uso
print(Calculadora.sumar(10, 5))
print(Calculadora.dividir(12, 4))
