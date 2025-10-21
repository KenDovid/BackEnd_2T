# 35. Convertir frase en slug (para URLs)
def slugify(s):
    import unicodedata
    s = s.lower()
    s = ''.join(c for c in unicodedata.normalize('NFD', s)
                if unicodedata.category(c) != 'Mn')
    s = s.replace(" ", "-")
    return ''.join(c for c in s if c.isalnum() or c == '-')

