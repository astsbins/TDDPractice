import unittest


def largest_prime_factor(n):
    if n < 2:
        return 0
    else:
        return n


class TestLargestPrimeFactor(unittest.TestCase):
    def test_n_is_1(self):
        self.assertEqual(0, largest_prime_factor(1))  # add assertion here

    def test_n_is_2(self):
        self.assertEqual(2, largest_prime_factor(2))

    def test_n_is_3(self):
        self.assertEqual(3, largest_prime_factor(3))

    def  test_n_is_4(self):
        self.assertEqual(2, largest_prime_factor(4))

if __name__ == '__main__':
    unittest.main()
