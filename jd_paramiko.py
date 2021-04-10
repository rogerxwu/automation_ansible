import paramiko
import time


def connect(ip,port,username,password):
    ssh_client = paramiko.SSHClient()
    ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    print(f'Connecting to {ip}')
    ssh_client.connect(hostname=ip, port=port, username= username, password= password, look_for_keys=False, allow_agent=False)
    return ssh_client

def get_shell(ssh_client):
    shell = ssh_client.invoke_shell()
    return shell

def send_command(shell, cmd, timeout=1):
    print(f'Sending command: {cmd}')
    shell.send(cmd + '\n')
    time.sleep(timeout)

def show(shell, n):
    output = shell.recv(n).decode()
    print(output)

def close(ssh_client):
    if ssh_client.get_transport().is_active() == True:
        print('Closing connection')
        ssh_client.close()

