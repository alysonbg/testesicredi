import unittest
from src.question2 import Orders


class TestOrders(unittest.TestCase):
    def test_return_the_ammount_of_travells(self):
        n_max = 100
        orders = Orders()

        self.assertEqual(2, orders.combine_orders([70, 30, 10], n_max))
        self.assertEqual(2, orders.combine_orders([70, 30, 10, 50], n_max))
