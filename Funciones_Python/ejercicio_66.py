# 66. Potencia recursiva (b >= 0)
def pow_rec(a, b):
    if b == 0:
        return 1
    return a * pow_rec(a, b - 1)

