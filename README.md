# EC2_jupyter_notebook

Start a jupyter notebook on EC2 server to speed up machine learning.

# Pre-requisites:
1. AWS Account
2. Python environment (Download python from www.python.org)
3. Boto3 and awscli
4. Key-pair file
5. existing EC2 server

<b>Note: If you havent set up your AWS account or installed boto3 and awscli please refer to the article on my website: https://vijayravi.blog/blog

# 1. Download ec2_start.py and ec2_stop.py files and save to working directory of your local command line. For example, mine is C:\Users\Vijay.

![Image description](https://github.com/vijay-ravi/EC2_jupyter_notebook/blob/master/Command_prompt.PNG)


# 2. Login to your AWS account and select a region of your choice
![Image description](https://github.com/vijay-ravi/EC2_jupyter_notebook/blob/master/region.PNG)

# 3. Create a key-pair file with .pem format and save the .pem file to to the working directory of your local command line.

![Image description](https://github.com/vijay-ravi/EC2_jupyter_notebook/blob/master/keypair.PNG)


# 4. Launch a linux EC2 instance based on your requirements.

![Image description](https://github.com/vijay-ravi/EC2_jupyter_notebook/blob/master/instance_type.PNG)


# 5. This is an important step. # In your security group, you need to allow inbound SSH port 22 and TCP port 8888.#

![Image description](https://github.com/vijay-ravi/EC2_jupyter_notebook/blob/master/security_group.PNG)


# 6. After your instance launches, copy the 'Instance ID' to clipboard. We will need it while editing python files.

![Image description](https://github.com/vijay-ravi/EC2_jupyter_notebook/blob/master/ec2_server.PNG)


# 7. Open up the ec2_start.py and ec2_stop.py files in any standard text editor (I use Atom. Atom rocks!) and paste the 'Instance ID' in the specified area. Also fill up the region name and .pem file name.

![Image description](https://github.com/vijay-ravi/EC2_jupyter_notebook/blob/master/code_edit.PNG)


# 8. Next step is to ssh into your ec2 server. Make sure the .pem file is in working directory of the command line Use the code: ssh -i #   insert .pem keyfile ec2-user@ insert public dns name

![Image description](https://github.com/vijay-ravi/EC2_jupyter_notebook/blob/master/ssh_1.PNG)


# 9. Download anaconda on your server using command: wget https://repo.anaconda.com/archive/Anaconda3-2019.10-Linux-x86_64.sh. You can also download miniconda environment if you want a minimal environmment: wget https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh
Refer https://repo.anaconda.com/archive and https://repo.anaconda.com/miniconda for relevant OS and python versions.

![Image description](https://github.com/vijay-ravi/EC2_jupyter_notebook/blob/master/get_anaconda.PNG)


# 10. Install using command: bash Anaconda3-2019.10-Linux-x86_64.sh 

![Image description](https://github.com/vijay-ravi/EC2_jupyter_notebook/blob/master/anaconda_install.PNG)


# 11. Now to start the jupyter server enter the below 3 commands:

    1. source .bashrc
    2. pip install jupyter
    3. jupyter notebook --no-browser
    
![Image description](https://github.com/vijay-ravi/EC2_jupyter_notebook/blob/master/jupyter_start.PNG)


# 12. Go to http://localhost:8000/ to get into the jupyter environment and create your notebooks. Refer https://www.youtube.com/watch?v=CR00meDBrPI if local host is not loading.


# 13. Now the fun stuff. After all that hard work, you definitely don't want to all that all again. The .py files that you have donwloaded will start or stop your EC2 servers as you execute just 1 line of code


# 14. Open up your command prompt and type the code:   python ec2_start.py  (This command assumes that you have the .pem file stored in working directory)

![Image description](https://github.com/vijay-ravi/EC2_jupyter_notebook/blob/master/jupyter_cmd.PNG)

# 15. Like before, go to http://localhost:8000/ to get into the jupyter environment.

![Image description](https://github.com/vijay-ravi/EC2_jupyter_notebook/blob/master/local_tree.PNG)

# 16. To stop the server all you need to do is run the command: python ec2_stop.py

![Image description](https://github.com/vijay-ravi/EC2_jupyter_notebook/blob/master/server_stop.PNG)


# Conclusion

Always remember to stop your EC2 servers to avoid accumulating charges. You can always check how much it is going to cost for different isntances over here: https://aws.amazon.com/ec2/pricing/on-demand/

So once you stop you EC2 instances, you wont be charged anymore but the EBS volumes that are attached to the EC2 instance still persist unless you manually delete them or checked 'Delete on Termination' when creating EC2 instance. But honestly EBS volumes are dirt cheap which start at $0.10 per GB-month of provisioned storage for General Purpose SSD (gp2) Volumes. That means even if you use 2 EBS volumes with 30 GB storage each running for 100 hours in month its going to cost just $0.8 USD. For calculations and pricing of EBS volumes refer here: https://aws.amazon.com/ebs/pricing/

The reason for keeping the EBS volumes is to avoid installing the anaconda environment all over on the new volume. But if you still wanna get rid of EBS volume and look for a cheaper alternative what you’ll want to do is create an AMI from your instance. Then you can even delete your instances, but still have all the work and files you created saved for future use. AMIs can also be saved in S3 for much less money by following these steps : http://docs.aws.amazon.com/AWSEC2/latest/UserGuide/creating-an-ami-instance-store.html



