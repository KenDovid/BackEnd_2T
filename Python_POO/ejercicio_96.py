# 📦 Ejercicio 96: Sistema de Envíos
# Modela paquetes, clientes y envíos con seguimiento.

class Cliente:
    def __init__(self, nombre):
        self.nombre = nombre

class Paquete:
    def __init__(self, id, peso):
        self.id = id
        self.peso = peso
        self.entregado = False

class Envio:
    def __init__(self, cliente, paquete):
        self.cliente = cliente
        self.paquete = paquete

    def entregar(self):
        self.paquete.entregado = True
        return f"Paquete {self.paquete.id} entregado a {self.cliente.nombre}"

# Uso
c = Cliente("Laura")
p = Paquete("PK001", 2.5)
e = Envio(c, p)
print(e.entregar())
