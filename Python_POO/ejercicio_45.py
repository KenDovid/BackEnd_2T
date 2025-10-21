# 🧮 Ejercicio 45: Método __iter__ — Iterar sobre Objetos
# Hace que una clase sea iterable con un bucle for.

class Agenda:
    def __init__(self):
        self.contactos = []

    def agregar_contacto(self, nombre):
        self.contactos.append(nombre)

    def __iter__(self):
        return iter(self.contactos)

# Uso
agenda = Agenda()
agenda.agregar_contacto("Ana")
agenda.agregar_contacto("Luis")
for contacto in agenda:
    print(contacto)
