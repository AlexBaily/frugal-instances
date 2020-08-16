from aws import get_instance_types, get_instance_price_history, get_most_expensive_instance, get_cheapest_instance_metric
from models import InstanceType

def main():

    instances = get_instance_types()
    for instance in instances:
        get_instance_price_history(instance, 10)
        instance.calculate_metric_cost("ram")
    most_expensive = get_most_expensive_instance(instances)
    cheapest_instance = get_cheapest_instance_metric(instances)
    print("name: ", most_expensive.name, " price:", most_expensive.max_price, "\n")
    print("name: ", cheapest_instance.name, " RAM: ", cheapest_instance.ram_gb, 
            " avg_cost: ", cheapest_instance.avg_price, 
            " metric_cost: ", cheapest_instance.metric_cost)


if __name__ == '__main__':
    main()
    