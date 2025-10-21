# 🔒 Ejercicio 21: Encapsulación Básica — Clase Cuenta con Atributos Privados
# Usa atributos privados para proteger los datos internos.

class Cuenta:
    def __init__(self, titular, saldo):
        self.__titular = titular
        self.__saldo = saldo

    def depositar(self, cantidad):
        if cantidad > 0:
            self.__saldo += cantidad
            return f"Depósito de ${cantidad}. Saldo actual: ${self.__saldo}"
        return "Cantidad inválida."

    def retirar(self, cantidad):
        if 0 < cantidad <= self.__saldo:
            self.__saldo -= cantidad
            return f"Retiro de ${cantidad}. Saldo restante: ${self.__saldo}"
        return "Fondos insuficientes o cantidad inválida."

    def consultar_saldo(self):
        return f"Saldo actual: ${self.__saldo}"

# Uso
cuenta = Cuenta("María", 500)
print(cuenta.depositar(300))
print(cuenta.retirar(200))
