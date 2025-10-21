# 💰 Ejercicio 3: Clase Cuenta Bancaria
# Modela una cuenta con métodos para depositar, retirar y consultar el saldo.

class CuentaBancaria:
    def __init__(self, saldo_inicial=0):
        self.saldo = saldo_inicial

    def depositar(self, cantidad):
        if cantidad > 0:
            self.saldo += cantidad
            return f"Depósito de {cantidad}. Nuevo saldo: {self.saldo}"
        return "Cantidad inválida."

    def retirar(self, cantidad):
        if cantidad > self.saldo:
            return "Saldo insuficiente."
        if cantidad > 0:
            self.saldo -= cantidad
            return f"Retiro de {cantidad}. Saldo restante: {self.saldo}"
        return "Cantidad inválida."

# Uso
cuenta = CuentaBancaria(1000)
print(cuenta.depositar(500))
print(cuenta.retirar(200))
