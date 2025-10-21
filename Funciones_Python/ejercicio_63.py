# 63. Sumar lista recursivamente
def sum_list_rec(lst):
    if not lst:
        return 0
    return lst[0] + sum_list_rec(lst[1:])


