# 11. Presentación con parámetro opcional
def presentacion(nombre, edad=0):
    if edad > 0:
        print(f"Hola, soy {nombre} y tengo {edad} años.")
    else:
        print(f"Hola, soy {nombre}.")

