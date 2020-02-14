# EC2_jupyter_notebook

Start a jupyter notebook on EC2 server to speed up machine learning.

# Pre-requisites:
1. AWS Account
2. Key-Pair file
3. Existing EC2 server

# Instructions:
1. Download ec2_start.py and ec2_stop.py files and save to working directory of your local command line. For example, mine is C:\Users\Vijay.

![Image description](https://github.com/vijay-ravi/EC2_jupyter_notebook/blob/master/Command_prompt.PNG)


2. Login to your AWS account and select a region of your choice

3. Create a key-pair file with .pem format and save the .pem file to to the working directory of your local command line.

![Image description](https://github.com/vijay-ravi/EC2_jupyter_notebook/blob/master/keypair.PNG)


4. Launch a linux EC2 instance based on your requirements.

![Image description](https://github.com/vijay-ravi/EC2_jupyter_notebook/blob/master/instance_type.PNG)


5. This is an important step. # In your security group, you need to allow inbound SSH port 22 and TCP port 8888.#

![Image description](https://github.com/vijay-ravi/EC2_jupyter_notebook/blob/master/security_group.PNG)

6. After your instance launches, stop your instance and copy the 'Instance ID' to clipboard. We will need it while editing python files.

![Image description](https://github.com/vijay-ravi/EC2_jupyter_notebook/blob/master/ec2_server.PNG)

7. Open up the ec2_start.py and ec2_stop.py files in any standard text editor (I use Atom. Atom rocks!) and paste the 'Instance ID' in the specified area. Also fill up the region name and .pem file name.

![Image description](https://github.com/vijay-ravi/EC2_jupyter_notebook/blob/master/code_edit.PNG)

8. Next download the AWS CLI from https://docs.aws.amazon.com/cli/latest/userguide/install-windows.html#install-msi-on-windows and install it.
