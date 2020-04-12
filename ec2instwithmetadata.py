import boto3

#Open a file to stoere the instaince ids.
 ofh = open('myinstdata.txt', 'r')
 for lines in ofh:
      
# read the content of the file.

# Check if the instance ids listed int he above file are running. 
# goto end of the program and siaply instance is already running.
# The istance in the file is nto runing or not found in AWS.
# now create the infraste.
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
# Apend the instnace ids creaed to the file.
# close the file.
