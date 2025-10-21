# 37. Comprobar si dos palabras son anagramas
def is_anagram(a, b):
    return sorted(a.replace(" ", "").lower()) == sorted(b.replace(" ", "").lower())

