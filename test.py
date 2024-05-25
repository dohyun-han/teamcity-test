import os
import paramiko
from io import StringIO

server_ip = '127.0.0.1'
username = 'han'
ssh_key_str = os.getenv('SSH_key')
ssh_key_fileobj = StringIO(ssh_key_str)
ssh_key = paramiko.RSAKey.from_private_key(ssh_key_fileobj)

def connect_ssh():
    ssh_client = paramiko.SSHClient()
    ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh_client.connect(server_ip, port=22, username=username, pkey=ssh_key)
    return ssh_client

client = connect_ssh()
client.close()
