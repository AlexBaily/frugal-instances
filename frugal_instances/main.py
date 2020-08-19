from aws import get_instance_types, get_instance_price_history, get_most_expensive_instance, get_cheapest_instance_metric
from aws import get_spot_reliability_data
from models import InstanceType
import logging
import json

def print_top_ten(instanceList):
    for x in range(10):
        print(instanceList[x].name, instanceList[x].ram_gb, instanceList[x].avg_price,
                instanceList[x].max_price)

def get_top_twenty_json(instanceList):
    instance_json = {"instances":[]}
    for x in range(20):
        instance_json['instances'].append(instanceList[x].to_json())
    return json.dumps(instance_json)


def parse_args():
    import argparse
    parser = argparse.ArgumentParser(
        description='Process spot instances and return the cheapest.')
    parser.add_argument('--metric', type=str, default='ram',
            help='Which metric do we want to use, cpu or ram')
    return parser.parse_args()

def main(metric=None):
    instances = get_instance_types()
    instanceList = list(instances)
    reliabilityJson = get_spot_reliability_data('eu-west-1')
    for instance in instanceList:
        get_instance_price_history(instance, 20)
        instance.calculate_metric_cost('ram')
        try: 
            instance.chance_of_term = reliabilityJson[instance.name]['r']
        except KeyError:
            logging.info('error: instance type not found' + instance.name)
    most_expensive = get_most_expensive_instance(instanceList)
    cheapest_instance = get_cheapest_instance_metric(instanceList)
    print("name: ", most_expensive.name, " price:", most_expensive.max_price, "\n")
    print("name: ", cheapest_instance.name, " RAM: ", cheapest_instance.ram_gb, 
            " avg_price: ", cheapest_instance.avg_price, 
            " metric_cost: ", cheapest_instance.metric_cost)
    #instanceList.sort(key=lambda x: x.metric_cost, reverse=False)
    best_instances = sorted((i for i in instanceList if i.chance_of_term == 0),
                            key=lambda x: x.metric_cost, reverse=False)
    #Print the top ten cheapest instances based on $ cost per GB of RAM.
    #print_top_ten(best_instances)
    print(get_top_twenty_json(best_instances))



if __name__ == '__main__':
    args = parse_args()
    main(metric=args.metric)
    

