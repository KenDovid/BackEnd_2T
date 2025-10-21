# 16. Mínimo y máximo sin usar min() ni max()
def min_max(*nums):
    if not nums:
        return None, None
    minimo = maximo = nums[0]
    for n in nums[1:]:
        if n < minimo:
            minimo = n
        if n > maximo:
            maximo = n
    return minimo, maximo

