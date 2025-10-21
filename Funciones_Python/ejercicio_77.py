# 77. Pruebas simples con assert
def suma(a, b):
    return a + b

def es_par(n):
    return n % 2 == 0

def invertir_lista(lst):
    return lst[::-1]


def test_functions():
    assert suma(2, 3) == 5
    assert es_par(4) is True
    assert invertir_lista([1, 2, 3]) == [3, 2, 1]
    print("✅ Todas las pruebas pasaron correctamente.")

