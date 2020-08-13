import unittest
from ..models import InstanceType


class TestInstanceType(unittest.TestCase):

    def test_max_price(self):
        instance = InstanceType(name="m4.xlarge", cpu=4, ram_gb=16)
        prices = [0.11, 0.22, 0.33, 0.55, 20]
        for price in prices:
            instance.add_price(prices)
        max_price = instance.max_price
        self.assertEqual(max_price, 20)
        