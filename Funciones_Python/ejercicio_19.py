# 19. Separar nombre y apellido
def split_name(fullname):
    partes = fullname.split(" ")
    if len(partes) >= 2:
        return partes[0], partes[1]
    return fullname, ""

