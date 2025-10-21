# 40. Convertir cadena 'k1=1;k2=2' a diccionario
def parse_key_value(s):
    pares = s.split(";")
    resultado = {}
    for p in pares:
        if "=" in p:
            k, v = p.split("=")
            resultado[k] = v
    return resultado