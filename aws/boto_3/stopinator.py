import boto3

client = boto3.client('ec2')

response = client.stop_instances(
    InstanceIds=[
        'i-0beef7c343f1656bf',
    ]
)

print(response)