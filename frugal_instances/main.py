import fmt
from aws import get_instance_types, get_instance_price_history, get_most_expensive_instance
from models import InstanceType

def main():

    instances = get_instance_types()
    for instance in instances:
        get_instance_price_history(instance)
    most_expensive = get_most_expensive_instance(instances)
    fmt.Printf("%v\n%v", most_expensive.name, most_expensive.max_price)


if __name__ == '__main__':
    main()
    