"""AWS Python SDK"""
import boto3

# Launching an EC2 instance (Ubuntu Server 18.04 LTS (HVM))
client = boto3.client('ec2')
resp = client.run_instances(
                ImageId='ami-079652134906bcbad',
                InstanceType='t2.micro',
                MinCount=1, MaxCount=1
                )
for instance in resp['Instances']:
    print(instance['InstanceId'])
