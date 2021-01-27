import unittest

from src.question1 import Contract
from src.question1 import Contracts


class TestContract(unittest.TestCase):
    def setUp(self):
        self.contracts = [
            Contract(1, 1),
            Contract(2, 2),
            Contract(3, 3),
            Contract(4, 4),
            Contract(5, 5)
        ]
        self.renegociated = [3]

    def test_get_top_N_open_contracts(self):
        contracts = Contracts()
        self.assertEqual([5, 4, 2], contracts.get_top_N_open_contracts(self.contracts, self.renegociated, 3))
