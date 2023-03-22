def sum_of_range(low_range: int, high_range: int) -> int:
    return sum_of_range_recursive(low_range, high_range)

    



def sum_of_range_loop(low_range: int, high_range: int) -> int:
    counter = 0
    for i in range(low_range, high_range+1):
        counter+= i
    return counter


def sum_of_range_recursive(low_range: int, high_range: int) -> int:
    if low_range == high_range:
        return low_range
    else:
        return low_range+sum_of_range_recursive(low_range+1,high_range)



print(sum_of_range(4,7))


