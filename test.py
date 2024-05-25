import os
import paramiko
from io import StringIO

server_ip = '172.22.158.9'
username = 'han'
ssh_key_str = os.getenv('SSH_key')
ssh_key_fileobj = StringIO(ssh_key_str)
ssh_key = paramiko.RSAKey.from_private_key(ssh_key_fileobj)

def connect_ssh():
    ssh_client = paramiko.SSHClient()
    ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh_client.connect(server_ip, port=22, username=username, pkey=ssh_key)
    return ssh_client

def create_file(filename, content):
    # 연결된 SSH 클라이언트 객체 가져오기
    client = connect_ssh()
    try:
        # 원하는 파일을 생성하고 내용을 쓰기
        stdin, stdout, stderr = client.exec_command(f'echo "{content}" > {filename}')
        print(stdout.read().decode())
        print(stderr.read().decode())
    finally:
        client.close()

create_file('test_file.txt', 'This is a test file created using SSH!')
