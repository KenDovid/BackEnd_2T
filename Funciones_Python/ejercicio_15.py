# 15. Promedio con número variable de argumentos
def promedio(*nums):
    if len(nums) == 0:
        return 0
    return sum(nums) / len(nums)


