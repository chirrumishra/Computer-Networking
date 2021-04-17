import socket
sock = socket.socket()
sock.connect(('127.0.0.1',1234))
print("Connection done")
#sock.send(input("Enter a string ").encode())
sock.send(b'Hi')
