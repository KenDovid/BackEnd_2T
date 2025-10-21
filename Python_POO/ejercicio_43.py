# 🧮 Ejercicio 43: Método __len__ y __getitem__
# Permite que una clase personalizada se comporte como una lista.

class Coleccion:
    def __init__(self, elementos):
        self.elementos = elementos

    def __len__(self):
        return len(self.elementos)

    def __getitem__(self, indice):
        return self.elementos[indice]

# Uso
numeros = Coleccion([10, 20, 30, 40])
print(len(numeros))
print(numeros[2])
