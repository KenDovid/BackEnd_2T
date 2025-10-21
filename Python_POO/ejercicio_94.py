# 🧾 Ejercicio 94: Sistema de Restaurante
# Mesas, pedidos y platos gestionados en conjunto.

class Plato:
    def __init__(self, nombre, precio):
        self.nombre = nombre
        self.precio = precio

class Pedido:
    def __init__(self, mesa):
        self.mesa = mesa
        self.platos = []

    def agregar_plato(self, plato):
        self.platos.append(plato)

    def total(self):
        return sum(p.precio for p in self.platos)

class Restaurante:
    def __init__(self):
        self.pedidos = []

    def crear_pedido(self, mesa):
        pedido = Pedido(mesa)
        self.pedidos.append(pedido)
        return pedido

# Uso
r = Restaurante()
p = r.crear_pedido(5)
p.agregar_plato(Plato("Pasta", 20))
p.agregar_plato(Plato("Café", 5))
print("Total mesa 5:", p.total())
