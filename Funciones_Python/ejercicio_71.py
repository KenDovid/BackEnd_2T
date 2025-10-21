# 71. Conversión segura a entero
def safe_int(s, default=0):
    try:
        return int(s)
    except ValueError:
        return default

