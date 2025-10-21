# 🚀 Ejercicio 38: Sistema de Vehículos con Polimorfismo
# Cada tipo de vehículo redefine cómo se mueve.

class Vehiculo:
    def mover(self):
        pass

class Avion(Vehiculo):
    def mover(self):
        return "✈️ Volando por los cielos."

class Tren(Vehiculo):
    def mover(self):
        return "🚆 Viajando por rieles."

class Bicicleta(Vehiculo):
    def mover(self):
        return "🚴 Avanzando por el camino."

# Uso
for v in [Avion(), Tren(), Bicicleta()]:
    print(v.mover())
