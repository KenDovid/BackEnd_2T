# 🧮 Ejercicio 87: Banco con Cuentas y Clientes
# Cada cliente puede tener múltiples cuentas con saldo independiente.

class Cuenta:
    def __init__(self, numero, saldo):
        self.numero = numero
        self.saldo = saldo

class Cliente:
    def __init__(self, nombre):
        self.nombre = nombre
        self.cuentas = []

    def agregar_cuenta(self, cuenta):
        self.cuentas.append(cuenta)

    def total_saldo(self):
        return sum(c.saldo for c in self.cuentas)

# Uso
cliente = Cliente("Andrea")
cliente.agregar_cuenta(Cuenta("001", 1500))
cliente.agregar_cuenta(Cuenta("002", 500))
print("Saldo total:", cliente.total_saldo())
