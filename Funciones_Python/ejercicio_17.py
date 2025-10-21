# 17. Verificar si una palabra es palíndromo
def es_palindromo(s, ignore_case=True):
    if ignore_case:
        s = s.lower()
    return s == s[::-1]

