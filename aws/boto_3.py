"""AWS Python SDK"""
import boto3

#====
# EC2
#====
# Launching an EC2 instance (Ubuntu Server 18.04 LTS (HVM))
ec2_client = boto3.client('ec2')
resp = ec2_client.run_instances(
                ImageId='ami-079652134906bcbad',
                InstanceType='t2.micro',
                MinCount=1, MaxCount=1
                )
for instance in resp['Instances']:
    print(instance['InstanceId'])


#==========
# Dynamodb
#==========

# INSTERT item onto dynamodb
dynamodb = boto3.client('dynamodb')
item = {
        "item_id": {"N": "1"},
        "name": {"S": "Nkanyezi"},
        "age": {"N": "3"}
        }
response = dynamodb.put_item(TableName='table_name', Item=item)

# INSTERT batch of items into dynamodb
ddb = boto3.resource('dynammodb')
table = ddb.Table('table-name')
with table.batch_writer() as batch:
    for x in range(1000):
        batch.put_item(Item={"item_id": {"N": f"{x}"}, "name": {"S": f"{x}"}})
        # batch.delete_item(Item={"item_id": {"N": f"{x}"}, "name": {"S": f"{x}"}})

# GET an item from dynamodb
ddb = boto3.resource('dynammodb')
table = ddb.Table('table-name')
response = table.get_item(Key={"item_id": "id"})

# DELETE an item from daynamodb
ddb = boto3.resource('dynammodb')
table = ddb.Table('table-name')
response = table.delete_item(Key={"item_id": "id"})