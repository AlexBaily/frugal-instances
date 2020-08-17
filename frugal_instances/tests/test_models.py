import unittest
from ..models import InstanceType


class TestInstanceType(unittest.TestCase):

    def test_max_price(self):
        instance = InstanceType(name="m4.xlarge", cpu=4, ram_gb=16)
        prices = [0.11, 0.22, 0.33, 0.55, 20]
        for price in prices:
            instance.add_price(price)
        max_price = instance.max_price
        self.assertEqual(max_price, 20)
        
    def test_calc_avg(self):
        instance = InstanceType(name="m4.xlarge", cpu=4, ram_gb=16)
        prices = [0.11, 0.22, 0.33, 0.55, 20]
        for price in prices:
            instance.add_price(price)
        instance.calc_avg()
        self.assertEqual(instance.avg_price, 4.242)

    def test_calc_metric_price(self):
        instance = InstanceType(name="m4.xlarge", cpu=4, ram_gb=16)
        prices = [0.11, 0.22, 0.33, 0.55, 20]
        for price in prices:
            instance.add_price(price)
        instance.calc_avg()
        instance.calculate_metric_cost("ram")
        self.assertEqual(instance.metric_cost, 0.265125)
