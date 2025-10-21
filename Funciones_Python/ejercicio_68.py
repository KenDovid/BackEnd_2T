# 68. Máximo común divisor (Euclides recursivo)
def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a % b)

