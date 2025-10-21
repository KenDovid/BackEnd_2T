# 🧩 Ejercicio 60: Herencia + Polimorfismo — Transporte Avanzado
# Cada tipo de transporte combina múltiples comportamientos heredados.

class Terrestre:
    def mover(self):
        return "Moviéndose sobre ruedas."

class Acuatico:
    def mover(self):
        return "Navegando sobre el agua."

class Anfibio(Terrestre, Acuatico):
    def mover(self):
        return f"Modo híbrido: {Terrestre.mover(self)} y {Acuatico.mover(self)}"

# Uso
vehiculo = Anfibio()
print(vehiculo.mover())
