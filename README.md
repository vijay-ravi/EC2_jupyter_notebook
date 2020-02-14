# EC2_jupyter_notebook

Start a jupyter notebook on EC2 server to speed up machine learning.

# Pre-requisites:
1. AWS Account
2. Python environment
3. Key-Pair file
4. EC2 server

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

6. After your instance launches, copy the 'Instance ID' to clipboard. We will need it while editing python files.

![Image description](https://github.com/vijay-ravi/EC2_jupyter_notebook/blob/master/ec2_server.PNG)

7. Open up the ec2_start.py and ec2_stop.py files in any standard text editor (I use Atom. Atom rocks!) and paste the 'Instance ID' in the specified area. Also fill up the region name and .pem file name.

![Image description](https://github.com/vijay-ravi/EC2_jupyter_notebook/blob/master/code_edit.PNG)

8. Next step is to ssh into your ec2 server. Make sure the .pem file is in working directory of the command line Use the code: ssh -i <insert .pem key file> ec2-user@ insert public dns name

![Image description](https://github.com/vijay-ravi/EC2_jupyter_notebook/blob/master/ssh_1.PNG)

9. Download anaconda on your server using command: wget https://repo.anaconda.com/archive/Anaconda3-2019.10-Linux-x86_64.sh

![Image description](https://github.com/vijay-ravi/EC2_jupyter_notebook/blob/master/get_anaconda.PNG)

10. Install using command: bash Anaconda3-2019.10-Linux-x86_64.sh 

![Image description](https://github.com/vijay-ravi/EC2_jupyter_notebook/blob/master/anaconda_install.PNG)

11. Now to start the jupyter server enter the below 2 commands:
    1. source .bashrc
    2. jupyter notebook --no-browser
    
![Image description](https://github.com/vijay-ravi/EC2_jupyter_notebook/blob/master/jupyter_start.PNG)

12. Go to http://localhost:8000/ to get into the jupyter environment and create your notebooks.

13. Now the fun stuff. After all that hard work, the next time you wanna start a server you dont need to do all the above. You just need two codes of line to get your notebook up and running. 

14. Open up your command prompt and type the code:   python ec2_start.py

![Image description](https://github.com/vijay-ravi/EC2_jupyter_notebook/blob/master/jupyter_cmd.PNG)

15. Like before, go to http://localhost:8000/ to get into the jupyter environment.

![Image description](https://github.com/vijay-ravi/EC2_jupyter_notebook/blob/master/local_tree.PNG)

16. To stop the server all you need to do is run the command: python ec2_stop.py

![Image description](https://github.com/vijay-ravi/EC2_jupyter_notebook/blob/master/server_stop.PNG)



