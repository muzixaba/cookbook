"""AWS Python SDK"""
import logging
import boto3

#===================
# Changing Profiles
#===================
# changing the default session
boto3.setup_default_session(profile_name='dev')

# using a specific creds
session = boto3.Session(
                aws_access_key_id="KEY_ID",
                aws_secret_access_key="SECRET_KEY",
                region_name="region")
s3 = session.client('s3')

# using a specific profile
session = boto3.Session(profile_name="my_profile")
s3 = session.client('s3')

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
        "item_id": {"N": str(1)},
        "name": {"S": "Nkanyezi"},
        "age": {"N": "3"},
        "height_in_meters": {"N": "1.2"}
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


#==========================
# Delete old EBS snapshots
#==========================

#!/usr/bin/env python
import boto3

MAX_SNAPSHOTS = 2   # Number of snapshots to keep

# Create the EC2 resource
ec2 = boto3.resource('ec2')

# Get a list of all volumes
volume_iterator = ec2.volumes.all()

# Create a snapshot of each volume
for v in volume_iterator:
  v.create_snapshot()

  # Too many snapshots?
  snapshots = list(v.snapshots.all())
  if len(snapshots) > MAX_SNAPSHOTS:

    # Delete oldest snapshots, but keep MAX_SNAPSHOTS available
    snap_sorted = sorted([(s.id, s.start_time, s) for s in snapshots], key=lambda k: k[1])
    for s in snap_sorted[:-MAX_SNAPSHOTS]:
      print("Deleting snapshot", s[0])
      s[2].delete()


#--------------------------------
# Using Boto3 with MFA enabled
#--------------------------------
#%%
client = boto3.client('sts')

response = client.get_session_token(
    DurationSeconds=900, # 15 mins
    SerialNumber='arn:aws:iam::account_number:mfa/username',
    TokenCode='mfa_code'
)

#%%
creds = response['Credentials']
session = boto3.Session(
    aws_access_key_id=creds["AccessKeyId"],
    aws_secret_access_key=creds["SecretAccessKey"],
    aws_session_token=creds["SessionToken"],
)

ec2 = session.client('ec2')


#===========================
# Decode Auth Error Messages
#===========================
import boto3
import argparse

# Parse command line arguments
parser = argparse.ArgumentParser()
parser.add_argument('-m', '--message', required=True, help='The AWS console authorization error message to decode')
args = parser.parse_args()

# Create an AWS client object
client = boto3.client('sts')

# Decode the authorization error message
response = client.decode_authorization_message(EncodedMessage=args.message)

# Print the decoded message to the console
print(response['DecodedMessage'])


# How to run
# python decode_auth_error.py -m <error_message>
