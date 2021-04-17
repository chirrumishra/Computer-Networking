import socket
sock = socket.socket()
sock.connect(('127.0.0.1',1234))
t = input("Enter file name ")
sock.send(t.encode())

print(sock.recv(1024).decode())
#print(sock.recv(1024).decode())
t=sock.recv(1024)
while(len(t)!=0):
    print(t.decode())
    t=sock.recv(1024)

