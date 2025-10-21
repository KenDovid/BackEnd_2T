# 20. División segura con valor de respaldo
def safe_divide(a, b, fallback=None):
    return a / b if b != 0 else fallback