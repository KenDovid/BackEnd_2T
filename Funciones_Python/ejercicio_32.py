# 32. Contar ocurrencias de un substring en un texto
def count_substring(s, sub):
    contador = 0
    pos = s.find(sub)
    while pos != -1:
        contador += 1
        pos = s.find(sub, pos + 1)
    return contador

