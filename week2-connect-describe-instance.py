import boto3

client = boto3.resource('ec2')
client.describe_instances()
client.describe_key_pairs()