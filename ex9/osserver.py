import socket
import os
sock=socket.socket(family = socket.AF_INET, type = socket.SOCK_DGRAM)
sock.bind(('127.0.0.1',1234))
t=sock.recvfrom(1024)
r=input("Enter the command ")
print(r)
#exec(r)
sock.sendto(r.encode(),t[1])
'''
t=sock.recvfrom(1024)
print(t[0].decode())
r=input("Enter the command")
r='os.system'+'('+r+')'
sock.sendto(r,t[1])
'''