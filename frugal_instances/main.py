from aws import get_instance_types, get_instance_price_history, get_most_expensive_instance, get_cheapest_instance_metric
from aws import get_spot_reliability_data
from models import InstanceType

def print_top_ten(instanceList):
    for x in range(10):
        print(instanceList[x].name, instanceList[x].ram_gb, instanceList[x].avg_price,
                instanceList[x].max_price)

def main():
    instances = get_instance_types()
    instanceList = list(instances)
    reliabilityJson = get_spot_reliability_data('eu-west-1')
    for instance in instanceList:
        get_instance_price_history(instance, 20)
        instance.calculate_metric_cost("ram")
        instance.chance_of_term = reliabilityJson[instance.name]['r']
    most_expensive = get_most_expensive_instance(instanceList)
    cheapest_instance = get_cheapest_instance_metric(instanceList)
    print("name: ", most_expensive.name, " price:", most_expensive.max_price, "\n")
    print("name: ", cheapest_instance.name, " RAM: ", cheapest_instance.ram_gb, 
            " avg_price: ", cheapest_instance.avg_price, 
            " metric_cost: ", cheapest_instance.metric_cost)
    #instanceList.sort(key=lambda x: x.metric_cost, reverse=False)
    best_instances = sorted(i for i in instanceList if i.chance_of_term <= 1,
                            key=lambda x: x.metric_cost, reverse=False)
    #Print the top ten cheapest instances based on $ cost per GB of RAM.
    print_top_ten(best_instances)



if __name__ == '__main__':
    main()
    

