# 💡 Ejercicio 18: Herencia y Polimorfismo — Instrumentos Musicales
# Todas las clases comparten la misma interfaz pero producen sonidos distintos.

class Instrumento:
    def tocar(self):
        return "Sonido genérico de instrumento."

class Guitarra(Instrumento):
    def tocar(self):
        return "🎸 Rasgueo de guitarra."

class Piano(Instrumento):
    def tocar(self):
        return "🎹 Notas de piano suaves."

class Bateria(Instrumento):
    def tocar(self):
        return "🥁 Golpes de batería potentes."

# Uso
for instrumento in [Guitarra(), Piano(), Bateria()]:
    print(instrumento.tocar())
