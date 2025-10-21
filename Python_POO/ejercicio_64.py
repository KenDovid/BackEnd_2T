# 💾 Ejercicio 64: Métodos de Clase para Crear Instancias Preconfiguradas
# Usa @classmethod para ofrecer alternativas de inicialización.

class Conexion:
    def __init__(self, host, puerto):
        self.host = host
        self.puerto = puerto

    @classmethod
    def por_defecto(cls):
        return cls("localhost", 8080)

# Uso
c1 = Conexion("192.168.1.1", 3000)
c2 = Conexion.por_defecto()
print(c1.host, c2.host)
