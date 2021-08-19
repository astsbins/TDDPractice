import unittest
from TDD_Tutorial.Basket import Basket

from TDD_Tutorial.Item import Item


class ShoppingBasketTest(unittest.TestCase):
    def test_empty_basket_total(self):
        basket = Basket([])
        self.assertEqual(0, basket.total())

    def test_single_item_quanitity_one(self):
        basket = Basket([Item(100, 1)])
        self.assertEqual(100, basket.total())

    def test_two_items_quantity_one(self):
        basket = Basket([Item(100, 1), Item(100, 1)])
        self.assertEqual(200, basket.total())

    def test_two_items_quantity_two(self):
        basket = Basket([Item(100, 2), Item(100,2)])
        self.assertEqual(200, basket.total())

if __name__ == "__main__":
    pass
