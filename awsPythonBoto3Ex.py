import boto3
import time


# Resource  this one returns Object, limited 
# Client  this one returns Dictionary, has access to all services 

# first let's setup a session
# create a user to access AWS console programatically 
# create a orfile for the user locally & use that user to login
# Create a session for that user

iam = boto3.session.Session(profile_name="samtest")


r1 = iam.resource('ec2')   # limited aws services, returns object 
r2 = iam.client('ec2')     # returns dictionary , more detailed , all resource 

# Instance = Class
# image_id = Attribute

x = "list of all instance"

ins = r1.Instance('i-0d9ef1dssafdSDSAFD')    # resource -> class -> attribute 

allec2 = r2.describe_instances()            # client -> method 

st = ins.state


# task start all instances 
# then stop instances that were stopped before 
# instances currenty in start  


# list of all instances that are stopped 

allec2 = r2.describe_instances()  # Dictionary
# 'InstanceId': 'i-0d9ef13d59f7edcfa'

# loop operation in Dictionary data type
resv = []

for i in allec2.values():
    resv.append(i)
    #print(type(i))

print(i)


'''

    def stpec2():
        stopd = []
        for ec2 in allec2:
            if(st == 'stopped'):
            stopd.append(ec2)
        print(stopd)


    #stpec2()

start = time.time()

stp  = []
strt = []
allin = []




for ec  in allec2['Reservations']:
  for i in ec['Instances']:
        j = i['InstanceId']
        allin.append(j)

for ec in allin:
            # if(r1.Instance(ec).state == "stopped"):
               # stp.append(ec)
            print(type(r1.Instance(ec).state.key()))
            #else:
            #    strt.append(ec)
       
##print(stp)
end = time.time() - start
#print(end)


'''

# 1. create  a python function that creates vpc, subnet & ec2
# 2. Create a function that List all VPC in your aws account
# 3. Create a function that list all EC2 using a Client function of Boto3


     
