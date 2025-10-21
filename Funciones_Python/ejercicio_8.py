# 8. Contar vocales en un texto
def contar_vocales(s):
    vocales = "aeiouAEIOU"
    return sum(1 for c in s if c in vocales)

