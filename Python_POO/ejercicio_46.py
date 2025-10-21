# 🔁 Ejercicio 46: Método __contains__ — Verificar Contenido
# Permite usar “in” para buscar dentro de un objeto.

class Catalogo:
    def __init__(self, productos):
        self.productos = productos

    def __contains__(self, producto):
        return producto in self.productos

# Uso
catalogo = Catalogo(["Tornillos", "Tuercas", "Clavos"])
print("Tuercas" in catalogo)
