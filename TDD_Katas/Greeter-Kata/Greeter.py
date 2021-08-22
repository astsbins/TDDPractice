from dataclasses import dataclass


@dataclass
class Time:
    hour: int


class Greeter:
    def __init__(self, time=Time(0)):
        self.cur_hour = time.hour

    def greet(self, name):
        name = name.strip()
        return f'{self.__get_greeting()}, {name}'

    def __get_greeting(self):
        if self.cur_hour >= 22:
            return 'Good Night'
        if self.cur_hour >= 18:
            return 'Good Evening'
        if self.cur_hour >= 12:
            return 'Good Afternoon'
        if self.cur_hour >= 6:
            return 'Good Morning'
        return "Hello"
