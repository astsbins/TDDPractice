def problem1(n):
    n = n - 1
    sum_all_multiples = 0
    sum_multiples_of_3 = n // 3
    sum_multiples_of_5 = n // 5
    sum_multiples_of_15 = n // 15
    sum_3_and_5_multiples = get_triangle_number(sum_multiples_of_3) * 3 + get_triangle_number(
        sum_multiples_of_5) * 5 - get_triangle_number(sum_multiples_of_15) * 15
    return sum_3_and_5_multiples


def get_triangle_number(n):
    if n % 2 == 0:
        return int(n ** 2 // 2 + n // 2)  # has to be integer division, took me far too long to figure out
    else:
        return int(n ** 2 // 2 + n // 2 + 1)
