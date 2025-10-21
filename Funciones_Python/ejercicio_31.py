# 31. Convertir texto a Title Case sin usar .title()
def title_case(s):
    palabras = s.split()
    return " ".join(p.capitalize() for p in palabras)


