import frugal_instances.aws

def main():

    instances = get_instance_types()
    for instance in instances:
        get_instance_price_history(instance)

if __name__ == '__main__':
    main()
    