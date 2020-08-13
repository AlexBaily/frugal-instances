import boto3
from datetime import datetime, timedelta
from models import InstanceType
'''
get_instance_types

Returns a list of all instance types available in the region.
Can return either just names or with info.
'''
def get_instance_types():
    ec2 = boto3.client('ec2')
    instance_types = set()
    #Filter for the API query. We don't want bare-metal instances.
    filters = [{"Name": "bare-metal","Values":["false"]}]
    response = ec2.describe_instance_types(Filters=filters)
    while True:
        #Run through instances, instantiate an InstanceType and then add to our set.
        for instance in response['InstanceTypes']: 
            instance_types.add(InstanceType(name=instance['InstanceType'], cpu=instance['VCpuInfo']['DefaultCores'],
                                    ram_gb=(instance['MemoryInfo']['SizeInMiB'] / 1024)))
        #Check if there is a NextToken to see if we need to deal with pagination.
        if 'NextToken' in response:
            response =  ec2.describe_instance_types(Filters=filters, NextToken=response['NextToken'])
        else:
            break 
    return instance_types


def get_instance_price_history(instance):
    ec2 = boto3.client('ec2')
    #Set the filters, we only want Linux Instance types.
    filters = [{"Name": "product-description", "Values":["Linux/UNIX", "Linux/UNIX (Amazon VPC)"]}]
    #Only grab info from the past 2 days.
    starttime = datetime.today() - timedelta(days=2)
    response = ec2.describe_spot_price_history(Filters=filters, InstanceTypes=[instance.name],
                                                StartTime=starttime)
    while True:
        for price_point in response['SpotPriceHistory']: 
            float_price = float(price_point['SpotPrice'])
            instance.add_price(float_price)
        #NextToken is always present in describe_spot_price_history so we just check if blank.
        if response['NextToken'] != '':
            response = ec2.describe_spot_price_history(Filters=filters, NextToken=response['NextToken'])
        else:
            instance.calc_avg()
            break 
    return

def get_most_expensive_instance(instances):
    most_expensive_instance = InstanceType
    for instance in instances:
        if instance.max_price > most_expensive:
            most_expensive = instance
    return most_expensive_instance


'''
def calculate_best_instance(instances, metric):
    lowest_cost = 0
    for instance in instances:
'''        