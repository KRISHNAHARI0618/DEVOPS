import boto3
import botocore

# import response


# EC2 instance details
ami_id = 'ami-0f3c7d07486cad139'  # replace with the desired AMI ID
instance_type = 't2.micro'
key_pair_name = 'DevOpsPracticeKey'  # replace with your key pair name

# Create an EC2 client

ec2 = boto3.client('ec2')
count = 20
# Create an EC2 instance
response = ec2.run_instances(
    ImageId=ami_id,
    InstanceType=instance_type,
    KeyName=key_pair_name,
    MinCount=1,
    MaxCount=count
)

print(type(response))


# for i in range(count):
#     print(response['Instances'][i]['InstanceId'])

# print(response['Instances'][0]['InstanceId'])
# instance_ids = []
# count = len(response['Instances'])
#
# # for  in response['Instances']:
# #     for j in
# #     print(i)

#
# for i in response['Instances']

# Extract the instance ID from the response
# instance_id = response['Instances'][0]['InstanceId']
# instance_id1 = response['Instances'][1]['InstanceId']
# print(f"EC2 instance created with ID: {instance_id}")
# print(f"EC2 instance created with ID: {instance_id1}")
