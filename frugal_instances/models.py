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
        self.chance_of_term = 5
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
        if self.avg_price <= 0:
            return
        if metric == "ram":
            self.metric_cost = self.avg_price /  self.ram_gb
        else:
            self.metric_cost = self.avg_price /  self.cpu
    def get_chance_string(self):
        rates = {
            0: "<5%",
            1: "5-10%",
            2: "10-15%",
            3: "15-20%",
            4: ">20%"
        }
        return rates[self.chance_of_term]
    def to_json(self):
        return {"name":self.name, "cpu":self.cpu, "ram":self.ram_gb, 
                "avg_price":self.avg_price, "max_price":self.max_price,
                "chance_of_term":self.get_chance_string()}