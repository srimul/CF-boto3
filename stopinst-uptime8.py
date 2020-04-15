import boto3
import dateutil.parser
import datetime

ec2=boto3.resource('ec2')
instances= ec2.instances.filter(Filters=[{'Name': 'instance-state-name', 'Values': ['running']}])
for i in instances:
    #print(i.launch_time)
    #print(i.launch_time.tzinfo)
    #print(datetime.datetime.utcnow())
    ec2_uptime = datetime.datetime.now(i.launch_time.tzinfo) - i.launch_time
    #print (ec2_uptime)
    uptime = str(ec2_uptime)
    uptimehr= uptime.split(":")[0]
    if int(uptimehr) >= 8:
        print("stopping server")
        i.stop()
    else:
        print("Running instances: "+ i.instance_id + " uptime:"+ uptime)
