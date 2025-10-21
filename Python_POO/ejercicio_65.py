# 🧩 Ejercicio 65: Método Estático para Validación de Datos
# Usa @staticmethod cuando no se necesita acceso a la instancia ni a la clase.

class Validador:
    @staticmethod
    def es_correo_valido(correo):
        return "@" in correo and "." in correo

# Uso
print(Validador.es_correo_valido("usuario@gmail.com"))
print(Validador.es_correo_valido("correo_invalido"))
