"""AWS Python SDK"""
import logging
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


#====
# S3
#====

# Create a bucket
s3_client = boto3.client('s3')
resp = s3_client.create_bucket(
                    ACL='private',
                    Bucket='bucket_name',
                    CreateBucketConfiguration={'LocationConstraint': 'af-south-1'}
                    )

# Upload readable file(s) to S3 bucket
s3_client = boto3.client('s3')
with open('path/to/file.ext', 'rb') as the_file:
    resp = s3_client.upload_fileobj(the_file, 'bucket_name', 'obj_name')

# Upload any file
def upload_file(file_name, bucket, obj_name=None):
    """Returns True if file was uploaded successfully, else False"""
    if obj_name is None:
        obj_name = file_name
    # initialise client & upload file
    s3 = boto3.client('s3')
    try:
        response = s3.upload_file(file_name, bucket, obj_name)
    except ClientError as e:
        logging.error(e)
        return False
    return True

# Delete object from s3 bucket
s3 = boto3.client('s3')
resp = s3.delete_object(
            Bucket='bucket_name',
            Key='object_name',
            )

# List objects inside s3 bucket
s3 = boto3.client('s3')
response = s3.list_objects(Bucket='bucket_name')

# List oll buckets
s3 = boto3.client('s3')
response = s3.list_buckets()

# Select data inside an s3 object
s3 = boto3.client('s3')
response = s3.select_object_content(
                    Bucket='bucket_name',
                    Key='file_name.csv',
                    Expression='Select s.name from S3Object s',
                    ExpressionType='SQL',
                    InputSerialization={"CSV": {'FileHeaderInfo': "Use"}},
                    OutputSerialization={"JSON", {}}
)