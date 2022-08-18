import boto3

#size to be modified
size="t2.large"
# Insert your Instance ID here
my_instance = <<some code here to fetch instance IDs of all instances 
filtering all t2.micro instance types>>

client = boto3.client('ec2')

# Stop the instance
client.stop_instances(InstanceIds=[my_instance])
waiter=client.get_waiter('instance_stopped')
waiter.wait(InstanceIds=[my_instance])

# Change the instance type
client.modify_instance_attribute(InstanceId=my_instance, 
Attribute='instanceType', Value=size)

# Start the instance
client.start_instances(InstanceIds=[my_instance])
