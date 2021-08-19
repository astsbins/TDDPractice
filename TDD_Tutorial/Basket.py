from dataclasses import dataclass
from functools import reduce
from typing import List
from Item import Item


@dataclass
class Basket():
    items: List[Item]

    def total(self):
        return reduce(lambda subtotal, item:  subtotal + item.unit_price * item.quantity, self.items, 0)

