# 🧬 Ejercicio 51: Herencia Múltiple Básica
# Combina dos clases base para crear una nueva que hereda de ambas.

class Volador:
    def volar(self):
        return "Estoy volando."

class Nadador:
    def nadar(self):
        return "Estoy nadando."

class Pato(Volador, Nadador):
    def sonido(self):
        return "Cuac, cuac!"

# Uso
pato = Pato()
print(pato.volar(), pato.nadar(), pato.sonido())
