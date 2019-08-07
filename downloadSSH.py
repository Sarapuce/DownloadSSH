from paramiko import SSHClient
from scp import SCPClient
from tqdm import tqdm

def download(ip, username, password, files, remote_path, client_path):

    if type(files) == str:
        files = [files]

    ssh = SSHClient()
    ssh.load_system_host_keys()
    ssh.connect(ip, username = username, password = password)
    
    scp = SCPClient(ssh.get_transport())
    
    for file_name in tqdm(df['file_path']):
    scp.get(remote_path = '{}/{}'.format(remote_path, file_name), 
            local_path = '{}/{}'.format(client_path, file_name))
    
    scp.close()