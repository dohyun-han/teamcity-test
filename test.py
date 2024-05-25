import os
import paramiko

server_ip = '127.0.0.1'
username = 'han'
ssh_key = os.getenv('env.SSH_key')

def connect_ssh():
    ssh_client = paramiko.SSHClient()
    ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh_client.connect(server_ip, port=22, username=username, pkey=ssh_key)
    return ssh_client

client = connect_ssh()
client.close()
