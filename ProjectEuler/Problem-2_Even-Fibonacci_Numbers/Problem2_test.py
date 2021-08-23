import unittest
from Problem2 import *


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
