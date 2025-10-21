# 🧠 Ejercicio 63: Decorador de Método — Validar Argumentos
# Usa un decorador dentro de una clase para validar los datos de entrada.

def validar_positivo(func):
    def envoltura(self, valor):
        if valor < 0:
            raise ValueError("El valor debe ser positivo.")
        return func(self, valor)
    return envoltura

class Banco:
    def __init__(self):
        self.saldo = 0

    @validar_positivo
    def depositar(self, cantidad):
        self.saldo += cantidad
        return f"Saldo actual: {self.saldo}"

# Uso
b = Banco()
print(b.depositar(100))
