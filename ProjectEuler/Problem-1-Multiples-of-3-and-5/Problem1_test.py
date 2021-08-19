import unittest
from Problem1 import problem1, get_triangle_number


class Problem1Test(unittest.TestCase):
    def test_N_is_0(self):
        self.assertEqual(0, problem1(0))

    def test_N_is_2(self):
        self.assertEqual(0, problem1(2))

    def test_N_is_3(self):
        self.assertEqual(3, problem1(4))

    def test_N_is_5(self):
        self.assertEqual(8, problem1(6))

    def test_multiple_boundary_lower(self):
        self.assertEqual(45, problem1(14))

    def test_multiple_boundary(self):
        self.assertEqual(45, problem1(15))

    def test_edge_case_n_39(self):
        self.assertEqual(329, problem1(39))

    def test_edge_case_n_40(self):
        self.assertEqual(368, problem1(40))

    def test_edge_case_n_41(self):
        self.assertEqual(408, problem1(41))

    def test_brute_force(self):
        sum_multiples = 0
        for i in range(1000000):
            if i % 3 == 0 or i % 5 == 0:
                sum_multiples += i
                self.assertEqual(sum_multiples, problem1(i + 1))

    def test_samples(self):
        self.assertEqual(23, problem1(10))
        self.assertEqual(2318, problem1(100))

    def test_triangle_number_1(self):
        self.assertEqual(1, get_triangle_number(1))
