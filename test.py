import os
import paramiko
from io import StringIO

ssh_key_content = os.getenv('SSH_key')

if not ssh_key_content:
    raise ValueError("MY_SSH_KEY.")

key_file = StringIO(ssh_key_content)
ssh_key = paramiko.RSAKey.from_private_key(key_file)

hostname = "your.server.com"
port = 22
username = "your_username"

ssh_client = paramiko.SSHClient()
ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())

print(ssh_key)