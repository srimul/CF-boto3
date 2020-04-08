import boto3

print("Start of the program")
ec2 = boto3.resource('ec2')

# create a new EC2 instance
instances = ec2.create_instances(
     ImageId='ami-0df2ea5740105c299',
     MinCount=1,
     MaxCount=1,
     InstanceType='t2.micro',
     KeyName='cZSecurityKey01'
)
print("AF Creation of ec2 instance")
print (type(instances))
print ( instances[0].id)
dir(instances)
print("After the dir command")
