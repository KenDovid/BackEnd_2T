# 39. Obtener iniciales de un nombre completo
def initials(fullname):
    partes = fullname.split()
    return ". ".join(p[0].upper() for p in partes) + "."

