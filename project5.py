import paramiko

router_ip = "172.30.86.56"
router_username = "admin"
router_password = "admin1"

ssh = paramiko.SSHClient()


# Connect to router using username/password authentication.
ssh.connect(router_ip, 
            username=router_username, 
            password=router_password,
            look_for_keys=False )

# Run commands


commands = ['configure terminal','hostname NewRouter','ssh_stdin, ssh_stdout, ssh_stderr = ssh.exec_command','copy running-config startup-config']
for command in commands:
    ssh_stdin, ssh_stdout, ssh_stderr = ssh.exec_command(command)
    error = ssh_stderr.readlines()
    if len(error) != 0:
        print(error)
# Close connection.
ssh.close()

