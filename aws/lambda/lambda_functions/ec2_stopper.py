import boto3
import json

def lambda_handler(event, context):
    """
    Stops all running instances in a given region.
    Needs a role that gives it access to EC2.
    Use EventBridge schedule rule to trigger lambda once a day.
    We'll use a CRON expression to trigger everyday at 7PM.
    e.g cron(0 17 * * ? *)
    NOTE: Cron expressions are written using UTC time,
    RSA is UTC+2, hence 17H00 in UTC is 19H00 to us
    """
    # Specify region
    region = 'eu-west-1'

    # get all running instances
    ec2 = boto3.client('ec2', region_name=region)
    response = ec2.describe_instances(
        Filters = [
            { 
            'Name': 'instance-state-name',
            'Values': ['running']
            },
        ]
    )

    # Retrieving instance ids, to know which ids are active on AWS
    running_instances = []
    for i in response['Reservations']:
        for e in i['Instances']:
            running_instances.append(e['InstanceId'])

    # Stop instance(s)
    if len(running_instances) > 0:
        ec2.stop_instances(InstanceIds=running_instances)
        print(f"Stopped Instances: {running_instances}")
        return {'statusCode': 200, 'body': json.dumps(f"Stopped: {running_instances}")}
    
    print("No instances needed to be stopped")
    return {'statusCode': 200, 'body': json.dumps("No instances needed to be stopped")}