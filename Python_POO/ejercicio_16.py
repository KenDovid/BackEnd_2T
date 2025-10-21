# 🏦 Ejercicio 16: Herencia con Sobrescritura — Sistema Bancario
# Las subclases especializan el comportamiento de una clase base de cuenta.

class Cuenta:
    def __init__(self, titular, saldo):
        self.titular = titular
        self.saldo = saldo

    def retirar(self, cantidad):
        if cantidad <= self.saldo:
            self.saldo -= cantidad
            return f"Retiro exitoso. Saldo: {self.saldo}"
        return "Fondos insuficientes."

class CuentaAhorros(Cuenta):
    def __init__(self, titular, saldo, interes):
        super().__init__(titular, saldo)
        self.interes = interes

    def aplicar_interes(self):
        self.saldo += self.saldo * self.interes
        return f"Interés aplicado. Nuevo saldo: {self.saldo:.2f}"

# Uso
ahorro = CuentaAhorros("María", 1000, 0.05)
print(ahorro.aplicar_interes())
