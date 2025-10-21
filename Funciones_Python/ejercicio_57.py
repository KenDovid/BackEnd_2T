# 57. Uso de nonlocal para modificar variable en closure
def nonlocal_demo():
    mensaje = "Hola"
    def cambiar():
        nonlocal mensaje
        mensaje = "Adiós"
    cambiar()
    return mensaje  # devuelve "Adiós"

