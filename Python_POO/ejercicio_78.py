# 🧠 Ejercicio 78: Excepciones Personalizadas
# Crea tu propia excepción para validar condiciones específicas.

class SaldoInsuficiente(Exception):
    pass

class Cuenta:
    def __init__(self, saldo):
        self.saldo = saldo

    def retirar(self, cantidad):
        if cantidad > self.saldo:
            raise SaldoInsuficiente("Fondos insuficientes.")
        self.saldo -= cantidad
        return f"Retiro exitoso. Saldo: {self.saldo}"

# Uso
try:
    cuenta = Cuenta(100)
    print(cuenta.retirar(150))
except SaldoInsuficiente as e:
    print("⚠️", e)
