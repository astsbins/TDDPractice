def problem2(max_fib_num):
    sum_even_fibs = 0
    fibs = find_fibonacci_numbers_less_than_n(max_fib_num)
    for fib in fibs:
        if fib % 2 == 0:
            sum_even_fibs += fib
            print(fib)
    return sum_even_fibs


def find_fibonacci_numbers_less_than_n(n):
    if n <= 1:
        return []
    elif n <= 2:
        return [1]
    elif n <= 3:
        return [1, 2]
    fib_list = [1, 2]
    while (fib_list[-1] + fib_list[-2]) < n:
        fib_list.append(fib_list[-1] + fib_list[-2])
    return fib_list