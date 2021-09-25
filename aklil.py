
#mysub="10.0.0.0/24" "10.0.0.16/24"
import boto3

def create_vpc_subnet_ec2():
    myami="ami-087c17d1fe0178315"
    myvpc="10.0.0.0/24"
    myclient=boto3.client('ec2')
    myvpcid=myclient.create_vpc(CidrBlock=myvpc)['Vpc']['VpcId']
    myclient.create_subnet(CidrBlock="10.0.0.0/28", VpcId=myvpcid)
    mysub=myclient.create_subnet(CidrBlock="10.0.0.32/28",VpcId=myvpcid)['Subnet']['SubnetId']
    myclient.run_instances(
        ImageId=myami,
        InstanceType='t2.micro',
        SubnetId=mysub,
        MinCount=1,
        MaxCount=1
    )
create_vpc_subnet_ec2()

def list_instances():
    ec2=boto3.client('ec2')
    paginator = ec2.get_paginator('describe_instances')
    for response in paginator.paginate():
       print(response)         
       print(type(response))       
       response['Reservations']
       for r in response['Reservations']:
           for i in r['Instances']:
                print(i['InstanceId'])
    
list_instances()

def lst_instance():
    client=boto3.client('ec2')
    response=client.describe_instances()
    for r in response['Reservations']:
        for i in r['Instances']:
           print(i['InstanceId'])
lst_instance()

def list_vpc():
    client=boto3.client('ec2')
    res=client.describe_vpcs()
    print(res)
    print(type(res))
    no_of_vpcs=res['Vpcs']
    print(len(no_of_vpcs))
    for vpc in no_of_vpcs:
            print(vpc['VpcId'])
list_vpc()