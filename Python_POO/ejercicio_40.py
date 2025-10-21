# 🧬 Ejercicio 40: Sistema de ADN — Comparación entre Cadenas
# Usa métodos especiales para comparar objetos con operadores.

class ADN:
    def __init__(self, secuencia):
        self.secuencia = secuencia.upper()

    def __eq__(self, otro):
        return self.secuencia == otro.secuencia

    def __len__(self):
        return len(self.secuencia)

# Uso
adn1 = ADN("ATCG")
adn2 = ADN("ATCG")
adn3 = ADN("TAGC")
print(adn1 == adn2, adn1 == adn3)
print("Longitud del ADN:", len(adn1))
