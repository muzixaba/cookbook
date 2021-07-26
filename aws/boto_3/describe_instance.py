import boto3

client = boto3.client('ec2')

# get info on all instances
response = client.describe_instances()


# print(response)
print(response["Reservations"][0]['Instances'][0]['ImageId'])