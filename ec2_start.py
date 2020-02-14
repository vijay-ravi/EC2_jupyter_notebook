import boto3
import pprint
import time
import os

def get_session(region):
    return boto3.session.Session(region_name=region)

def countdown(t):
    while t:
        mins, secs = divmod(t, 60)
        timeformat = '{:02d}:{:02d}'.format(mins, secs)
        print(timeformat, end='\r')
        time.sleep(1)
        t -= 1
    pprint.pprint(instance.state)

session= get_session('insert region name here')
ec2 = session.resource('ec2')
instance = ec2.Instance('insert instance id here')
pprint.pprint(instance.start())
countdown(30)
pprint.pprint(instance.state)
dns_name = instance.public_dns_name
ip = instance.public_ip_address

os.system(f'cmd /k "ssh -i 'insert .pem file here' -L 8000:localhost:8888 ec2-user@{dns_name} jupyter notebook --no-browser"')
