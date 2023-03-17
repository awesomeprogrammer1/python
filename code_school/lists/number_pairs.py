"""
Дан список чисел. Если в нем есть два соседних элемента одного знака, выведите эти числа. Если соседних элементов одного знака нет — не выводите ничего. Если таких пар соседей несколько — выведите первую пару.
"""

def number_pairs(lst: list) -> list:
    if len(lst) > 1:
        for i in range(len(lst)-1):
            if lst[i] >= 0 and lst[i+1] >= 0 or lst[i] < 0 and lst[i+1] < 0:
                return [lst[i], lst[i+1]]
        else:
            return []
    else:
        return []
