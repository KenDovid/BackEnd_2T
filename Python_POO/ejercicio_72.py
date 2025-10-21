# 🧱 Ejercicio 72: Patrón Factory — Creador de Objetos según Parámetro
# Devuelve diferentes tipos de objetos según un valor dado.

class Auto:
    def mover(self): return "El auto se desplaza por carretera."

class Avion:
    def mover(self): return "El avión surca los cielos."

class Barco:
    def mover(self): return "El barco navega en el mar."

class TransporteFactory:
    @staticmethod
    def crear_transporte(tipo):
        if tipo == "auto": return Auto()
        elif tipo == "avion": return Avion()
        elif tipo == "barco": return Barco()
        else: raise ValueError("Tipo de transporte inválido.")

# Uso
vehiculo = TransporteFactory.crear_transporte("barco")
print(vehiculo.mover())
