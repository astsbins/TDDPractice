import unittest


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


class Problem2Test(unittest.TestCase):
    def test_n_1(self):
        self.assertEqual(0, problem2(1))

    def test_n_3(self):
        self.assertEqual(2, problem2(3))

    def test_n_5(self):
        self.assertEqual(2, problem2(5))

    def test_n_10(self):
        self.assertEqual(10, problem2(10))

    def test_n_100(self):
        self.assertEqual(44, problem2(100))

    def test_find_fibonacci_n1(self):
        self.assertEqual([], find_fibonacci_numbers_less_than_n(1))

    def test_find_fibonacci_n2(self):
        self.assertEqual([1], find_fibonacci_numbers_less_than_n(2))

    def test_find_fibonacci_n3(self):
        self.assertEqual([1, 2], find_fibonacci_numbers_less_than_n(3))

    def test_find_fibonacci_n4(self):
        self.assertEqual([1, 2, 3], find_fibonacci_numbers_less_than_n(4))

    def test_find_fibonacci_n4(self):
        self.assertEqual([1, 2, 3, 5,8], find_fibonacci_numbers_less_than_n(10))

    def test_find_fibonacci_large(self):
        self.assertEqual([1, 2, 3, 5, 8, 13], find_fibonacci_numbers_less_than_n(14))

        if __name__ == '__main__':
            unittest.main()
