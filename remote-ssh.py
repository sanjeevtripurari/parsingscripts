#!/usr/bin/python3
import paramiko, sys, getpass

if len(sys.argv) > 1:
	hostname = sys.argv[1]
	username = sys.argv[2]
	message  = sys.argv[3]
	password = getpass.getpass()
else:
	(hostname,username,password)=('192.168.90.20','vagrant','vagrant')
	message='default values'

client = paramiko.SSHClient()
client.set_missing_host_key_policy(paramiko.AutoAddPolicy)
client.connect(hostname, username=username, password=password)
stdin, stdout, stderr = client.exec_command('echo Message: '+message)
stdin.close()
print(repr(stdout.read()))
stdout.close()
stderr.close()

print("\nUptime")
stdin, stdout, stderr = client.exec_command('uptime')
stdin.close()
print(repr(stdout.read()))
stdout.close()
stderr.close()

print("\nDisk Usage")
stdin, stdout, stderr = client.exec_command('df -h')
stdin.close()
print(repr(stdout.read()))
stdout.close()
stderr.close()

print("\nFree Mem")
stdin, stdout, stderr = client.exec_command('free -g')
stdin.close()
print(repr(stdout.read()))
stdout.close()
stderr.close()

client.close
