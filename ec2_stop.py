import boto3
import pprint
import time

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
pprint.pprint(instance.stop())
print('Stopping in 60 sec......')
countdown(60)
pprint.pprint(instance.wait_until_stopped())
