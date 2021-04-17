import socket
sock = socket.socket()
port = 1234
sock.bind(('',1234))
sock.listen(10)

r,addr = sock.accept()
print("Connection done")
print("The string received is")
#print(r.recv(1024).decode())
print(r.recv(1024))
