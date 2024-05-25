import os
import paramiko
from io import StringIO

# 환경 변수에서 SSH 키 내용 가져오기
ssh_key_content = os.getenv('SSH_key')

if not ssh_key_content:
    raise ValueError("MY_SSH_KEY 환경 변수가 설정되지 않았습니다.")

# Paramiko를 사용하여 SSH 키 로드
key_file = StringIO(ssh_key_content)
ssh_key = paramiko.RSAKey.from_private_key(key_file)

# 서버 정보
hostname = "your.server.com"
port = 22
username = "your_username"

# Paramiko를 사용하여 SSH 연결 설정
ssh_client = paramiko.SSHClient()
ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())

print(ssh_key)