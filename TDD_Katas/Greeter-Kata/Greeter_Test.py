import unittest

from Greeter import Greeter, Time


class TestGreeter(unittest.TestCase):
    def test_greeting(self):
        greeter = Greeter()
        self.assertEqual("Hello, jason", greeter.greet("jason"))

    def test_greeting_trim(self):
        greeter = Greeter()
        self.assertEqual("Hello, jason", greeter.greet("jason  "))

    def test_greeting_trim(self):
        greeter = Greeter()
        self.assertEqual("Hello, jason", greeter.greet("jason  "))

    def test_get_time(self):
        time = Time(hour=2)
        self.assertEqual(2, time.hour)

    def test_greeting_morning(self):
        greeter = Greeter(Time(hour=6))
        self.assertEqual("Good Morning, jason", greeter.greet("jason  "))

    def test_greeting_afternoon(self):
        greeter = Greeter(Time(hour=12))
        self.assertEqual("Good Afternoon, jason", greeter.greet("jason  "))

    def test_greeting_evening(self):
        greeter = Greeter(Time(hour=18))
        self.assertEqual("Good Evening, jason", greeter.greet("jason  "))

    def test_greeting_night(self):
        greeter = Greeter(Time(hour=22))
        self.assertEqual("Good Night, jason", greeter.greet("jason  "))


if __name__ == '__main__':
    unittest.main()
