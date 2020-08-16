import sys

class InstanceType:
    def __init__(self, name, cpu, ram_gb):
        self.name = name
        self.cpu = cpu
        self.ram_gb = ram_gb
        self.prices = []
        self.avg_price = 0.0
        self.max_price = 0.0
        self.calc_cost = sys.maxsize
        self.metric_cost = sys.maxsize
    def calc_avg(self):
        if sum(self.prices) > 0:
            self.avg_price = (sum(self.prices) / len(self.prices))
        else:
            self.avg_price = sys.maxsize
    def add_price(self, price):
        self.prices.append(price)
        if price > self.max_price:
            self.max_price = price
    def calculate_metric_cost(self, metric):
        if metric == "ram":
            self.instance.metric_cost = self.instance.avg_price /  self.instance.ram_gb
        else:
            self.instance.metric_cost = self.instance.avg_price /  self.instance.cpu
