# 🔄 Ejercicio 88: Sistema de Reservas de Hotel
# Habitaciones, clientes y reservas interconectadas.

class Habitacion:
    def __init__(self, numero, tipo):
        self.numero = numero
        self.tipo = tipo
        self.ocupada = False

class Reserva:
    def __init__(self, cliente, habitacion):
        self.cliente = cliente
        self.habitacion = habitacion
        habitacion.ocupada = True

class Cliente:
    def __init__(self, nombre):
        self.nombre = nombre
        self.reservas = []

    def hacer_reserva(self, habitacion):
        if not habitacion.ocupada:
            reserva = Reserva(self, habitacion)
            self.reservas.append(reserva)
            return f"Reserva exitosa de la habitación {habitacion.numero}"
        return "La habitación ya está ocupada."

# Uso
c = Cliente("Lucía")
h1 = Habitacion(101, "Suite")
print(c.hacer_reserva(h1))
