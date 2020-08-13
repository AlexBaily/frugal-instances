from aws import get_instance_types, get_instance_price_history
from models import InstanceType

def main():

    instances = get_instance_types()
    for instance in instances:
        get_instance_price_history(instance)

if __name__ == '__main__':
    main()
    