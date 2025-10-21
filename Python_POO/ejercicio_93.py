# 🚗 Ejercicio 93: Sistema de Alquiler de Autos
# Gestiona vehículos disponibles y su estado de alquiler.

class Auto:
    def __init__(self, marca):
        self.marca = marca
        self.disponible = True

class Alquiler:
    def __init__(self, auto, cliente):
        self.auto = auto
        self.cliente = cliente
        auto.disponible = False

class Agencia:
    def __init__(self):
        self.autos = []

    def registrar_auto(self, auto):
        self.autos.append(auto)

    def alquilar(self, marca, cliente):
        for a in self.autos:
            if a.marca == marca and a.disponible:
                return Alquiler(a, cliente)
        return "Auto no disponible."

# Uso
ag = Agencia()
ag.registrar_auto(Auto("Toyota"))
print(ag.alquilar("Toyota", "Lucía"))

