# 🧠 Ejercicio 22: Encapsulación con Getters y Setters
# Controla el acceso a un atributo privado usando propiedades.

class Persona:
    def __init__(self, nombre, edad):
        self.__nombre = nombre
        self.__edad = edad

    @property
    def edad(self):
        return self.__edad

    @edad.setter
    def edad(self, nueva_edad):
        if 0 <= nueva_edad <= 120:
            self.__edad = nueva_edad
        else:
            raise ValueError("Edad inválida.")

# Uso
p = Persona("Laura", 25)
print(p.edad)
p.edad = 30
print(p.edad)
