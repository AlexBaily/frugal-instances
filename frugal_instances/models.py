import sys


class InstanceType:

    def __init__(self, name, cpu, ram):
        self.name = name
        self.cpu = cpu
        self.ram = ram
        self.prices = []
        self.calc_cost = sys.maxsize

    