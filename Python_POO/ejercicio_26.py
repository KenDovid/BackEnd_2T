# 💳 Ejercicio 26: Polimorfismo Aplicado — Métodos de Pago
# Distintos tipos de pago usan el mismo método “procesar_pago”.

class MetodoPago:
    def procesar_pago(self):
        pass

class TarjetaCredito(MetodoPago):
    def procesar_pago(self):
        return "Pago procesado con tarjeta de crédito."

class Efectivo(MetodoPago):
    def procesar_pago(self):
        return "Pago realizado en efectivo."

class Transferencia(MetodoPago):
    def procesar_pago(self):
        return "Pago efectuado por transferencia bancaria."

# Uso
for metodo in [TarjetaCredito(), Efectivo(), Transferencia()]:
    print(metodo.procesar_pago())
