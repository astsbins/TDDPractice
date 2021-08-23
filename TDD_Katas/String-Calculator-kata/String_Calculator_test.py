import unittest

def string_addd():
    pass

class MyTestCase(unittest.TestCase):
    def test_something(self):
        self.assertEqual(None, string_addd())  # add assertion here


if __name__ == '__main__':
    unittest.main()
